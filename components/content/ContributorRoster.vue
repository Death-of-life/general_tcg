<script setup lang="ts">
defineProps<{
  title?: string
  description?: string
  items: Array<{
    name: string
    handle?: string
    title?: string
    body: string
  }>
}>()
</script>

<template>
  <div class="my-8 space-y-4">
    <div v-if="title || description" class="space-y-2">
      <h3 v-if="title" class="text-xl font-semibold text-highlighted">{{ title }}</h3>
      <p v-if="description" class="text-sm leading-7 text-muted">{{ description }}</p>
    </div>

    <div class="space-y-4">
      <UCard
        v-for="item in items"
        :key="`${item.name}-${item.handle || ''}`"
        class="paper-panel rounded-[1.5rem]"
      >
        <div class="grid gap-4 lg:grid-cols-[16rem_1fr]">
          <div class="space-y-1">
            <h4 class="text-2xl font-semibold text-highlighted">{{ item.name }}</h4>
            <p v-if="item.handle" class="text-sm text-muted">{{ item.handle }}</p>
            <p v-if="item.title" class="text-sm leading-7 text-toned">{{ item.title }}</p>
          </div>

          <p class="text-sm leading-8 text-toned">{{ item.body }}</p>
        </div>
      </UCard>
    </div>
  </div>
</template>
