import { defineCollection, defineContentConfig, z } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    docs: defineCollection({
      type: 'page',
      source: 'docs/**/*.md',
      schema: z.object({
        title: z.string(),
        description: z.string(),
        order: z.number(),
        section: z.string(),
        sourcePageStart: z.number(),
        sourcePageEnd: z.number(),
        draft: z.boolean().default(false),
        sourceLanguage: z.string().default('ja'),
        terms: z.array(z.string()).default([])
      })
    })
  }
})

