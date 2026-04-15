<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  description?: string
  opponentLife: number | string
  playerLife: number | string
  opponentHand: number | string
  playerHand: number | string
  opponentBoard: string[]
  playerBoard: string[]
  handCards: string[]
  footnote?: string
}>(), {
  opponentBoard: () => [],
  playerBoard: () => [],
  handCards: () => []
})
</script>

<template>
  <UCard class="paper-panel my-8 rounded-[1.6rem]">
    <template #header>
      <div class="space-y-2">
        <h3 class="text-xl font-semibold text-highlighted">{{ title }}</h3>
        <p v-if="description" class="text-sm leading-7 text-muted">{{ description }}</p>
      </div>
    </template>

    <div class="rounded-[1.35rem] border border-default/70 bg-elevated/70 p-4">
      <div class="space-y-6 rounded-[1.15rem] border border-default/70 bg-default/45 p-5">
        <div class="grid gap-4 md:grid-cols-[1fr_auto] md:items-start">
          <div>
            <p class="text-sm uppercase tracking-[0.18em] text-dimmed">Opponent</p>
            <div class="mt-2 flex flex-wrap gap-2">
              <UBadge color="neutral" variant="outline">生命 {{ opponentLife }}</UBadge>
              <UBadge color="neutral" variant="outline">手牌 {{ opponentHand }}</UBadge>
            </div>
          </div>

          <div class="grid min-h-20 grid-cols-2 gap-3 sm:grid-cols-3">
            <div
              v-for="card in opponentBoard"
              :key="card"
              class="flex min-h-20 items-center justify-center rounded-[1rem] border border-default/70 bg-default/80 px-3 text-center text-sm leading-6 text-toned"
            >
              {{ card }}
            </div>
          </div>
        </div>

        <USeparator />

        <div class="grid gap-4 md:grid-cols-[1fr_auto] md:items-start">
          <div>
            <p class="text-sm uppercase tracking-[0.18em] text-dimmed">You</p>
            <div class="mt-2 flex flex-wrap gap-2">
              <UBadge color="primary" variant="soft">生命 {{ playerLife }}</UBadge>
              <UBadge color="primary" variant="soft">手牌 {{ playerHand }}</UBadge>
            </div>
          </div>

          <div class="grid min-h-20 grid-cols-2 gap-3 sm:grid-cols-3">
            <div
              v-for="card in playerBoard"
              :key="card"
              class="flex min-h-20 items-center justify-center rounded-[1rem] border border-primary/30 bg-primary/10 px-3 text-center text-sm leading-6 text-toned"
            >
              {{ card }}
            </div>
          </div>
        </div>

        <div class="space-y-3">
          <p class="text-sm uppercase tracking-[0.18em] text-dimmed">手中可用资源</p>
          <div class="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
            <div
              v-for="card in handCards"
              :key="card"
              class="flex min-h-24 items-center justify-center rounded-[1rem] border border-default/70 bg-default/80 px-4 text-center text-sm leading-6 text-toned"
            >
              {{ card }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <p v-if="footnote" class="doc-caption mt-4">{{ footnote }}</p>
  </UCard>
</template>
