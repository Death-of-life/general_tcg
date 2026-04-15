<script setup lang="ts">
defineProps<{
  title: string
  description?: string
  steps: Array<{
    title: string
    detail?: string
  }>
  footnote?: string
}>()
</script>

<template>
  <UCard class="paper-panel my-8 rounded-[1.6rem]">
    <template #header>
      <div class="space-y-2">
        <h3 class="text-xl font-semibold text-highlighted">{{ title }}</h3>
        <p v-if="description" class="text-sm leading-7 text-muted">{{ description }}</p>
      </div>
    </template>

    <div class="space-y-3 rounded-[1.35rem] border border-default/70 bg-elevated/70 p-4">
      <template v-for="(step, index) in steps" :key="step.title">
        <div class="rounded-[1.2rem] border border-default/70 bg-default/70 px-4 py-4">
          <div class="flex gap-4">
            <div class="flex size-10 shrink-0 items-center justify-center rounded-full border border-primary/40 bg-primary/10 font-semibold text-primary">
              {{ index + 1 }}
            </div>

            <div class="space-y-1">
              <h4 class="text-lg font-semibold text-highlighted">{{ step.title }}</h4>
              <p v-if="step.detail" class="text-sm leading-7 text-toned">{{ step.detail }}</p>
            </div>
          </div>
        </div>

        <div
          v-if="index !== steps.length - 1"
          class="mx-auto flex size-8 items-center justify-center rounded-full bg-primary/10 text-primary"
        >
          <UIcon name="i-lucide-arrow-down" class="size-4" />
        </div>
      </template>
    </div>

    <p v-if="footnote" class="doc-caption mt-4">{{ footnote }}</p>
  </UCard>
</template>
