<script setup lang="ts">
import type { ChapterMapItem } from '~/lib/content-data'

const props = defineProps<{
  chapter: ChapterMapItem
}>()
</script>

<template>
  <UCard class="paper-panel h-full rounded-[1.5rem]">
    <template #header>
      <div>
        <div>
          <p class="text-xs uppercase tracking-[0.22em] text-dimmed">{{ chapter.category }}</p>
          <h3 class="mt-2 text-xl font-semibold text-highlighted">{{ chapter.titleZh }}</h3>
          <p class="mt-1 text-sm text-muted">{{ chapter.titleJa }}</p>
        </div>
      </div>
    </template>

    <p class="text-sm leading-7 text-toned">
      {{ chapter.summary }}
    </p>

    <div class="mt-5 flex items-center justify-between gap-3 text-sm text-muted">
      <span>源页码 {{ chapter.sourcePageStart }} - {{ chapter.sourcePageEnd }}</span>

      <UButton
        v-if="chapter.publishedPath"
        label="进入章节"
        :to="chapter.publishedPath"
        trailing-icon="i-lucide-arrow-right"
        color="primary"
        variant="soft"
      />
    </div>
  </UCard>
</template>
