<script setup lang="ts">
const props = defineProps<{
  title: string
  tone?: 'insight' | 'warning' | 'info'
}>()

const toneMeta = computed<{ color: 'primary' | 'warning' | 'info', icon: string }>(() => {
  if (props.tone === 'warning') {
    return { color: 'warning', icon: 'i-lucide-triangle-alert' }
  }

  if (props.tone === 'info') {
    return { color: 'info', icon: 'i-lucide-badge-info' }
  }

  return { color: 'primary', icon: 'i-lucide-sparkles' }
})
</script>

<template>
  <UAlert
    :title="title"
    :color="toneMeta.color"
    :icon="toneMeta.icon"
    variant="soft"
    class="my-8 rounded-[1.4rem]"
  >
    <template #description>
      <div class="paper-prose text-sm">
        <slot />
      </div>
    </template>
  </UAlert>
</template>
