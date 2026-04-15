<script setup lang="ts">
import type { ContentNavigationItem } from '@nuxt/content'
import type { NavigationMenuItem } from '@nuxt/ui'
import type { Ref } from 'vue'
import { zh_cn } from '@nuxt/ui/locale'

const route = useRoute()

const headerLinks = computed<NavigationMenuItem[]>(() => [
  {
    label: '首页',
    to: '/',
    active: route.path === '/'
  },
  {
    label: '文库',
    to: '/docs',
    active: route.path.startsWith('/docs')
  }
])

const { data: navigation } = await useAsyncData('docs-navigation', () => {
  return queryCollectionNavigation('docs')
    .where('draft', '=', false)
    .order('order', 'ASC')
})

const { data: files } = await useAsyncData('docs-search-files', () => {
  return queryCollectionSearchSections('docs')
    .where('draft', '=', false)
    .order('order', 'ASC')
})

provide('docs-navigation', navigation as Ref<ContentNavigationItem[] | undefined>)
</script>

<template>
  <UApp :locale="zh_cn">
    <div class="mx-auto flex min-h-screen max-w-[1600px] flex-col px-4 py-4 md:px-6">
      <UHeader class="paper-panel rounded-[1.75rem] border border-default/70 px-4 md:px-6">
        <template #title>
          <AppLogo />
        </template>

        <UNavigationMenu :items="headerLinks" />

        <template #right>
          <UContentSearchButton />
          <UColorModeButton />
        </template>

        <template #body>
          <UNavigationMenu :items="headerLinks" orientation="vertical" class="-mx-2.5" />
        </template>
      </UHeader>

      <UMain class="flex-1 py-6">
        <NuxtLayout>
          <NuxtPage />
        </NuxtLayout>
      </UMain>

      <UFooter class="paper-panel rounded-[1.75rem] border border-default/70 px-4 py-5 md:px-6">
        <template #left>
          <div class="space-y-1 text-sm text-muted">
            <p>《一般 TCG 理论》中文文档站</p>
            <p>静态部署版</p>
          </div>
        </template>

        <template #right>
          <div class="space-y-1 text-sm text-muted">
            <p>基于 Nuxt Content</p>
            <p>面向长文阅读与 LLM 抓取</p>
          </div>
        </template>
      </UFooter>
    </div>

    <UContentSearch
      :navigation="navigation"
      :files="files"
      title="检索文档与章节"
      description="输入标题、术语或正文片段，直接跳到对应章节。"
    />
  </UApp>
</template>
