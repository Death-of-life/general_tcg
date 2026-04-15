<script setup lang="ts">
const props = defineProps<{
  title?: string
  description?: string
  rows: Array<Record<string, string>>
  footnote?: string
}>()

const columns = computed(() => {
  const keys = Array.from(new Set(props.rows.flatMap(row => Object.keys(row))))

  return keys.map(key => ({
    accessorKey: key,
    header: key
  }))
})
</script>

<template>
  <div class="my-8 space-y-4">
    <div v-if="title || description" class="space-y-2">
      <h3 v-if="title" class="text-xl font-semibold text-highlighted">{{ title }}</h3>
      <p v-if="description" class="text-sm leading-7 text-muted">{{ description }}</p>
    </div>

    <div class="overflow-hidden rounded-[1.4rem] border border-default/70 bg-elevated/80">
      <UTable :data="rows" :columns="columns" sticky="header" />
    </div>

    <p v-if="footnote" class="doc-caption">{{ footnote }}</p>
  </div>
</template>

