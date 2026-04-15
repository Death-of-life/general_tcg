<script setup lang="ts">
import type { ContentNavigationItem } from '@nuxt/content'
import type { Ref } from 'vue'

const navigation = inject<Ref<ContentNavigationItem[] | undefined>>('docs-navigation')
</script>

<template>
  <div class="page-surface rounded-[2rem] px-4 py-5 md:px-6 md:py-6">
    <UPage>
      <template #left>
        <UPageAside class="paper-panel rounded-[1.5rem] border border-default/70 p-4">
          <div class="mb-4 flex items-center justify-between">
            <p class="text-xs uppercase tracking-[0.2em] text-dimmed">已发布文档</p>
            <UBadge color="primary" variant="soft">Docs</UBadge>
          </div>

          <UContentNavigation :navigation="navigation || []" />
        </UPageAside>
      </template>

      <slot />
    </UPage>
  </div>
</template>
