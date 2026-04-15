<script setup lang="ts">
defineProps<{
  src: string
  alt: string
  caption?: string
  credit?: string
}>()
</script>

<template>
  <figure class="my-8 space-y-3">
    <div class="overflow-hidden rounded-[1.5rem] border border-default/70 bg-elevated shadow-sm">
      <img :src="src" :alt="alt" class="w-full object-cover" loading="lazy">
    </div>

    <figcaption v-if="caption || credit" class="doc-caption">
      <span v-if="caption">{{ caption }}</span>
      <span v-if="credit"> · {{ credit }}</span>
    </figcaption>
  </figure>
</template>

