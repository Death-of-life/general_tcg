#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz


@dataclass
class ChapterItem:
    slug: str
    title_zh: str
    title_ja: str
    source_page_start: int
    source_page_end: int
    category: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Extract text, metadata and chapter bundles from a PDF.')
    parser.add_argument('--pdf', required=True, help='Path to the source PDF.')
    parser.add_argument('--output', required=True, help='Directory for extracted page files and manifest.')
    parser.add_argument('--chapter-map', required=False, help='JSON file describing chapter ranges.')
    parser.add_argument('--chapter-output', required=False, help='Directory for chapter source bundles.')
    parser.add_argument('--public-output', required=False, help='Directory for preview images.')
    parser.add_argument('--preview-pages', default='', help='Comma-separated 1-based pages to render as WebP previews.')
    return parser.parse_args()


def clean_text(value: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', value).strip()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def render_preview(doc: fitz.Document, page_number: int, output_dir: Path) -> str:
    ensure_dir(output_dir)
    page = doc.load_page(page_number - 1)
    pix = page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
    output_path = output_dir / f'page-{page_number:03d}.png'
    pix.save(output_path)
    return str(output_path)


def load_chapters(path: Path | None) -> list[ChapterItem]:
    if not path:
        return []

    raw = json.loads(path.read_text(encoding='utf-8'))
    chapters: list[ChapterItem] = []

    for item in raw:
        chapters.append(
            ChapterItem(
                slug=item['slug'],
                title_zh=item['titleZh'],
                title_ja=item['titleJa'],
                source_page_start=int(item['sourcePageStart']),
                source_page_end=int(item['sourcePageEnd']),
                category=item['category']
            )
        )

    return chapters


def write_page_markdown(page_number: int, text: str, page_dir: Path) -> Path:
    ensure_dir(page_dir)
    path = page_dir / f'page-{page_number:03d}.md'
    path.write_text(
        f'# 第 {page_number} 页\n\n{text}\n',
        encoding='utf-8'
    )
    return path


def write_chapter_bundle(chapter: ChapterItem, pages: dict[int, str], output_dir: Path) -> None:
    chapter_dir = output_dir / chapter.slug
    ensure_dir(chapter_dir)

    parts = []
    for page_number in range(chapter.source_page_start, chapter.source_page_end + 1):
        text = pages.get(page_number, '').strip()
        parts.append(f'## 第 {page_number} 页\n\n{text or "（本页未提取到可用文本）"}')

    source_markdown = '\n\n'.join(parts).strip() + '\n'
    frontmatter = {
        'titleZh': chapter.title_zh,
        'titleJa': chapter.title_ja,
        'category': chapter.category,
        'sourcePageStart': chapter.source_page_start,
        'sourcePageEnd': chapter.source_page_end
    }

    (chapter_dir / 'meta.json').write_text(
        json.dumps(frontmatter, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8'
    )
    (chapter_dir / 'source.md').write_text(source_markdown, encoding='utf-8')


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf).resolve()
    output_dir = Path(args.output).resolve()
    pages_dir = output_dir / 'pages'
    ensure_dir(output_dir)
    ensure_dir(pages_dir)

    chapter_output = Path(args.chapter_output).resolve() if args.chapter_output else None
    public_output = Path(args.public_output).resolve() if args.public_output else None
    preview_pages = {
        int(item)
        for item in args.preview_pages.split(',')
        if item.strip().isdigit()
    }

    chapters = load_chapters(Path(args.chapter_map).resolve()) if args.chapter_map else []
    doc = fitz.open(pdf_path)

    page_text_lookup: dict[int, str] = {}
    manifest_pages: list[dict[str, Any]] = []
    preview_manifest: list[dict[str, Any]] = []

    for index in range(doc.page_count):
        page_number = index + 1
        page = doc.load_page(index)
        text = clean_text(page.get_text('text'))
        page_text_lookup[page_number] = text
        markdown_path = write_page_markdown(page_number, text, pages_dir)

        image_entries = []
        for image_index, image in enumerate(page.get_images(full=True)):
            xref = image[0]
            width = image[2]
            height = image[3]
            image_entries.append({
                'index': image_index,
                'xref': xref,
                'width': width,
                'height': height
            })

        manifest_pages.append({
          'page': page_number,
          'width': round(page.rect.width, 2),
          'height': round(page.rect.height, 2),
          'charCount': len(text),
          'textFile': str(markdown_path.relative_to(output_dir)),
          'textPreview': text[:240],
          'embeddedImages': image_entries
        })

        if public_output and page_number in preview_pages:
            preview_path = render_preview(doc, page_number, public_output / 'page-previews')
            preview_manifest.append({
                'page': page_number,
                'file': preview_path
            })

    manifest = {
        'sourcePdf': str(pdf_path),
        'generatedAt': datetime.now(timezone.utc).isoformat(),
        'pageCount': doc.page_count,
        'metadata': {
            'title': doc.metadata.get('title'),
            'author': doc.metadata.get('author'),
            'creator': doc.metadata.get('creator'),
            'producer': doc.metadata.get('producer')
        },
        'pages': manifest_pages,
        'previewImages': preview_manifest
    }

    (output_dir / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8'
    )

    if chapter_output:
        ensure_dir(chapter_output)
        for chapter in chapters:
            write_chapter_bundle(chapter, page_text_lookup, chapter_output)

    print(json.dumps({
        'pdf': str(pdf_path),
        'pageCount': doc.page_count,
        'output': str(output_dir),
        'chapters': len(chapters),
        'previews': len(preview_manifest)
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
