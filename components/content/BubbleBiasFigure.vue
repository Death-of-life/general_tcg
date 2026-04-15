<script setup lang="ts">
type BubbleItem = {
  label: string
  note?: string
  x: number
  y: number
  size: 'sm' | 'md' | 'lg'
}

withDefaults(defineProps<{
  title: string
  description?: string
  leftAxisLabel?: string
  rightAxisLabel?: string
  items: BubbleItem[]
}>(), {
  leftAxisLabel: '内部因素',
  rightAxisLabel: '外部因素'
})

const bubbleSizes = {
  sm: '7.5rem',
  md: '10rem',
  lg: '13rem'
} as const
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
      <div class="relative h-[28rem] overflow-hidden rounded-[1.15rem] border border-default/70 bg-default/40">
        <div
          v-for="item in items"
          :key="item.label"
          class="absolute flex items-center justify-center rounded-full border border-default/70 bg-primary/18 text-center shadow-sm backdrop-blur"
          :style="{
            left: `${item.x}%`,
            top: `${item.y}%`,
            width: bubbleSizes[item.size],
            height: bubbleSizes[item.size],
            transform: 'translate(-50%, -50%)'
          }"
        >
          <div class="space-y-1 px-3">
            <p class="text-base font-semibold text-highlighted">{{ item.label }}</p>
            <p v-if="item.note" class="text-xs leading-5 text-toned">{{ item.note }}</p>
          </div>
        </div>

        <div class="absolute inset-x-10 bottom-8 flex items-center gap-3 text-sm text-muted">
          <span>{{ leftAxisLabel }}</span>
          <div class="h-px flex-1 bg-primary/40" />
          <span>{{ rightAxisLabel }}</span>
        </div>
      </div>
    </div>
  </UCard>
</template>
