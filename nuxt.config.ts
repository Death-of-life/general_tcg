import chapterMap from './data/chapter-map.json'
import terminology from './data/terminology.json'

const publishedChapterCount = chapterMap.filter(chapter => chapter.status === 'published').length
const llmsTerminologyNotes = terminology.slice(0, 6).map(term => {
  return `${term.term}（${term.original}）: ${term.translation}。${term.note}`
})

export default defineNuxtConfig({
  compatibilityDate: '2025-02-15',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@nuxt/content', 'nuxt-llms'],
  ui: {
    fonts: false
  },
  css: ['~/assets/css/main.css'],
  app: {
    head: {
      htmlAttrs: {
        lang: 'zh-CN'
      },
      titleTemplate: '%s · 一般 TCG 理论文库',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: '围绕《一般TCG理论》搭建的中文文档站，收录导论、章节路线图、术语表与 LLM 友好的原始 Markdown 输出。'
        }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }
      ]
    }
  },
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/', '/docs', '/llms.txt', '/llms-full.txt']
    }
  },
  llms: {
    domain: process.env.NUXT_PUBLIC_SITE_URL || 'http://localhost:3000',
    title: '一般 TCG 理论文库',
    description: `围绕《一般TCG理论》整理的简体中文文档站，当前已发布 ${publishedChapterCount} 个章节，覆盖导论、正文、附录与后记。`,
    sections: [
      {
        title: '站点入口',
        description: '先从首页了解项目定位，再进入导论与文章章节。',
        links: [
          {
            title: '首页',
            description: '项目简介、阅读路径、章节状态总览。',
            href: '/'
          },
          {
            title: '阅读导引',
            description: '文档站使用方式、翻译策略与阅读建议。',
            href: '/docs'
          },
          {
            title: '原始 PDF',
            description: '用于建立页码映射与术语校对的源文件。',
            href: '/General_TCG_Theory_single.pdf'
          }
        ]
      },
      {
        title: '已发布章节',
        description: '只收录已翻译、已排版完成、可供 LLM 与读者直接消费的页面。',
        contentCollection: 'docs',
        contentFilters: [
          {
            field: 'draft',
            operator: '=',
            value: false as unknown as string
          },
          {
            field: 'extension',
            operator: '=',
            value: 'md'
          }
        ]
      }
    ],
    notes: [
      `全书共拆分为 ${chapterMap.length} 个章节单元；当前站点已完整发布正文、附录与后记。`,
      'llms.txt 默认改写为 /raw/docs/*.md，以便模型读取原始 Markdown 而非页面 HTML。',
      ...llmsTerminologyNotes
    ],
    full: {
      title: '一般 TCG 理论全文输出',
      description: '汇总所有已发布章节的原始中文 Markdown，供 LLM 高效抓取与全文检索。'
    },
    contentRawMarkdown: {
      rewriteLLMSTxt: true,
      excludeCollections: []
    }
  },
  runtimeConfig: {
    public: {
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'http://localhost:3000'
    }
  }
})
