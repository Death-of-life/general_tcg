<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  description?: string
  stages: [string, string, string]
  leftNote?: string
  rightNote?: string
  footnote?: string
}>(), {
  leftNote: '',
  rightNote: ''
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

    <div class="rounded-[1.35rem] border border-default/70 bg-elevated/70 p-4">
      <div class="grid gap-6 lg:grid-cols-[0.8fr_1fr_0.8fr] lg:items-center">
        <div v-if="leftNote" class="text-sm leading-7 text-toned">{{ leftNote }}</div>

        <div class="relative mx-auto flex size-[20rem] items-center justify-center rounded-full bg-primary/8">
          <div class="absolute inset-7 rounded-full bg-secondary/12" />
          <div class="absolute inset-[5.5rem] rounded-full bg-primary/20" />
          <div class="absolute inset-0 flex items-start justify-center pt-10">
            <span class="text-2xl font-semibold text-highlighted">{{ stages[0] }}</span>
          </div>
          <div class="absolute inset-0 flex items-center justify-center">
            <span class="text-2xl font-semibold text-highlighted">{{ stages[1] }}</span>
          </div>
          <div class="absolute inset-0 flex items-end justify-center pb-10">
            <span class="text-2xl font-semibold text-highlighted">{{ stages[2] }}</span>
          </div>
          <div class="absolute left-9 top-1/2 -translate-y-1/2 text-primary">
            <UIcon name="i-lucide-arrow-down" class="size-10 -rotate-45" />
          </div>
          <div class="absolute right-9 top-[30%] text-secondary">
            <UIcon name="i-lucide-arrow-up" class="size-10 rotate-45" />
          </div>
        </div>

        <div v-if="rightNote" class="text-sm leading-7 text-toned">{{ rightNote }}</div>
      </div>
    </div>

    <p v-if="footnote" class="doc-caption mt-4">{{ footnote }}</p>
  </UCard>
</template>
