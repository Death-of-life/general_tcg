<script setup lang="ts">
defineProps<{
  term: string
  original: string
  translation: string
  description: string
}>()
</script>

<template>
  <UCard class="paper-panel my-8 rounded-[1.4rem]">
    <template #header>
      <div class="flex flex-wrap items-center gap-3">
        <UBadge color="primary" variant="soft">{{ term }}</UBadge>
        <span class="text-sm text-muted">{{ original }}</span>
      </div>
    </template>

    <div class="space-y-2 text-sm leading-7 text-toned">
      <p><span class="font-medium text-highlighted">统一译法：</span>{{ translation }}</p>
      <p>{{ description }}</p>
    </div>
  </UCard>
</template>

