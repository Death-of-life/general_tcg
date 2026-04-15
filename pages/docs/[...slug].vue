<script setup lang="ts">
import type { ContentNavigationItem } from '@nuxt/content'
import { findChapterByPath } from '~/lib/content-data'

const route = useRoute()

definePageMeta({
  layout: 'docs'
})

const { data: page } = await useAsyncData(route.path, () => {
  return queryCollection('docs').path(route.path).first()
})

if (!page.value) {
  throw createError({
    statusCode: 404,
    statusMessage: '文档不存在'
  })
}

const resolvedPage = computed(() => page.value!)

const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
  return queryCollectionItemSurroundings('docs', route.path, {
    fields: ['title', 'description']
  }).where('draft', '=', false).order('order', 'ASC')
})

const { data: navigation } = await useAsyncData('docs-breadcrumb-navigation', () => {
  return queryCollectionNavigation('docs').where('draft', '=', false).order('order', 'ASC')
})

const chapter = computed(() => findChapterByPath(route.path))

const breadcrumb = computed(() => {
  const items: Array<{ label: string, to: string }> = [
    { label: '文库', to: '/docs' }
  ]

  const pages = (navigation.value || []) as ContentNavigationItem[]

  function visit(
    nodes: ContentNavigationItem[],
    trail: Array<{ label: string, to: string }> = []
  ): Array<{ label: string, to: string }> | undefined {
    for (const node of nodes) {
      const nextTrail = node.path ? [...trail, { label: node.title || '', to: node.path }] : trail

      if (node.path === route.path) {
        return nextTrail
      }

      if (node.children?.length) {
        const found = visit(node.children, nextTrail)
        if (found) {
          return found
        }
      }
    }

    return undefined
  }

  return [...items, ...(visit(pages) || []).filter((item: { label: string, to: string }) => item.to !== '/docs')]
})

useSeoMeta({
  title: resolvedPage.value.title,
  description: resolvedPage.value.description
})
</script>

<template>
  <UPage>
    <UPageHeader :title="resolvedPage.title" :description="resolvedPage.description">
      <template #headline>
        <UBreadcrumb :items="breadcrumb" />
      </template>

      <div class="article-meta">
        <UBadge color="primary" variant="soft">
          {{ resolvedPage.section }}
        </UBadge>
        <UBadge color="neutral" variant="outline">
          源页码 {{ resolvedPage.sourcePageStart }} - {{ resolvedPage.sourcePageEnd }}
        </UBadge>
        <UBadge color="neutral" variant="outline">
          原文语言 {{ (resolvedPage.sourceLanguage || 'ja').toUpperCase() }}
        </UBadge>
        <UBadge v-if="chapter" color="success" variant="soft">
          章节映射已锁定
        </UBadge>
      </div>
    </UPageHeader>

    <UPageBody class="paper-prose">
      <ContentRenderer :value="resolvedPage" />

      <USeparator class="my-10" />

      <UContentSurround :surround="surround" />
    </UPageBody>

    <template #right>
      <UPageAside class="paper-panel rounded-[1.5rem] border border-default/70 p-4">
        <p class="mb-3 text-xs uppercase tracking-[0.2em] text-dimmed">本页目录</p>
        <UContentToc :links="resolvedPage.body?.toc?.links || []" />

        <div v-if="resolvedPage.terms?.length" class="mt-6 space-y-3 border-t border-default/70 pt-4">
          <p class="text-xs uppercase tracking-[0.2em] text-dimmed">关键词</p>
          <div class="flex flex-wrap gap-2">
            <UBadge
              v-for="term in resolvedPage.terms"
              :key="term"
              color="primary"
              variant="soft"
            >
              {{ term }}
            </UBadge>
          </div>
        </div>
      </UPageAside>
    </template>
  </UPage>
</template>
