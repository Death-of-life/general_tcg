# 一般 TCG 理论文库

基于 Nuxt 4、@nuxt/ui、@nuxt/content 与 `nuxt-llms` 搭建的中文文档站，用来整理 `General_TCG_Theory_single.pdf` 的章节映射、中文精翻与 LLM 友好输出。

## 常用命令

```bash
pnpm install
pnpm dev
pnpm typecheck
pnpm generate
pnpm preprocess:pdf
```

## 目录说明

- `content/docs/`：已发布的中文页面。
- `data/chapter-map.json`：章节映射的单一事实源。
- `data/terminology.json`：翻译、注释与 llms 共用的术语表。
- `scripts/preprocess_pdf.py`：把 PDF 转成页级文本清单、章节源文件和预览图。
- `.baoyu-skills/baoyu-translate/EXTEND.md`：项目级翻译偏好。

## LLM 输出

- `/llms.txt`：结构化概览。
- `/llms-full.txt`：已发布内容的全文输出。
- `/raw/docs/*.md`：给模型抓取的原始 Markdown。

