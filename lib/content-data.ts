import chapterMapJson from '../data/chapter-map.json'
import terminologyJson from '../data/terminology.json'

export type ChapterStatus = 'published' | 'planned'

export interface ChapterMapItem {
  id: string
  slug: string
  titleZh: string
  titleJa: string
  summary: string
  category: string
  status: ChapterStatus
  sourcePageStart: number
  sourcePageEnd: number
  publishedPath?: string
}

export interface TerminologyEntry {
  term: string
  original: string
  translation: string
  note: string
}

export const chapterMap = chapterMapJson as ChapterMapItem[]
export const terminology = terminologyJson as TerminologyEntry[]

export const chapterStats = {
  total: chapterMap.length,
  published: chapterMap.filter(chapter => chapter.status === 'published').length,
  planned: chapterMap.filter(chapter => chapter.status === 'planned').length
}

export const publishedChapters = chapterMap.filter(chapter => chapter.status === 'published')

export function findChapterByPath(path: string) {
  return chapterMap.find(chapter => chapter.publishedPath === path)
}

export function statusLabel(status: ChapterStatus) {
  return status === 'published' ? '已发布' : '待翻译'
}

