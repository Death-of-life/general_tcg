<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  description?: string
  thresholdLabel?: string
  leftLabel: string
  rightLabel: string
  assumptions?: string[]
  footnote?: string
}>(), {
  thresholdLabel: '50%',
  assumptions: () => []
})
</script>

<template>
  <UCard class="paper-panel my-8 overflow-hidden rounded-[1.6rem]">
    <template #header>
      <div class="space-y-2">
        <h3 class="text-xl font-semibold text-highlighted">{{ title }}</h3>
        <p v-if="description" class="text-sm leading-7 text-muted">{{ description }}</p>
      </div>
    </template>

    <div class="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
      <div class="space-y-3">
        <div class="rounded-[1.35rem] border border-default/70 bg-elevated/70 p-4">
          <div class="relative mx-auto h-48 max-w-xl overflow-hidden rounded-[1.1rem] border border-default/70 bg-default/30">
            <div class="absolute inset-y-4 left-4 w-[42%] rounded-full bg-primary/12" />
            <div class="absolute inset-y-4 right-4 w-[42%] rounded-full bg-secondary/12" />
            <div class="absolute inset-x-8 top-1/2 h-1 -translate-y-1/2 bg-primary/70" />
            <div class="absolute left-[12%] top-1/2 size-4 -translate-y-1/2 rounded-full border-2 border-primary/80 bg-default" />
            <div class="absolute left-1/2 top-1/2 size-4 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-primary/80 bg-default" />
            <div class="absolute right-[12%] top-1/2 size-4 -translate-y-1/2 rounded-full border-2 border-primary/80 bg-default" />
            <p class="absolute left-[9%] top-[56%] text-sm text-muted">0%</p>
            <p class="absolute left-1/2 top-[56%] -translate-x-1/2 text-sm font-medium text-highlighted">{{ thresholdLabel }}</p>
            <p class="absolute right-[8%] top-[56%] text-sm text-muted">100%</p>
            <p class="absolute left-[14%] top-[22%] max-w-28 text-center text-sm leading-6 text-toned">{{ leftLabel }}</p>
            <p class="absolute right-[14%] top-[22%] max-w-28 text-center text-sm leading-6 text-toned">{{ rightLabel }}</p>
          </div>
        </div>
      </div>

      <div class="space-y-3">
        <div
          v-for="assumption in assumptions"
          :key="assumption"
          class="rounded-[1.15rem] border border-default/70 bg-default/55 px-4 py-3 text-sm leading-7 text-toned"
        >
          {{ assumption }}
        </div>
      </div>
    </div>

    <p v-if="footnote" class="doc-caption mt-4">{{ footnote }}</p>
  </UCard>
</template>
