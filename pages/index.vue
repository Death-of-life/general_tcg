<script setup lang="ts">
import { chapterMap } from '~/lib/content-data'

const sections = [
  {
    title: '导论',
    description: '先理解一般 TCG 理论的目标，以及作者为何从这里开始。',
    icon: 'i-lucide-book-open-text'
  },
  {
    title: '文章',
    description: '围绕概率、数据、构筑、大局观、直觉与教学展开正文。',
    icon: 'i-lucide-scroll-text'
  },
  {
    title: '附录与后记',
    description: '补足跨学科例子、作者寄语与终章收束。',
    icon: 'i-lucide-bookmark'
  }
]

useSeoMeta({
  title: '首页',
  description: '《一般 TCG 理论》中文文档站首页。'
})
</script>

<template>
  <div class="space-y-8">
    <section class="page-surface overflow-hidden rounded-[2rem] px-4 py-6 md:px-6 md:py-8">
      <div class="grid gap-8 lg:grid-cols-[1.1fr_0.9fr]">
        <div class="space-y-6">
          <span class="hero-kicker">General TCG Theory</span>

          <div class="space-y-4">
            <h1 class="max-w-4xl text-4xl font-semibold tracking-tight text-highlighted md:text-6xl">
              《一般 TCG 理论》
              中文文档站
            </h1>

            <p class="max-w-3xl text-base leading-8 text-toned md:text-lg">
              这里收录本书的简体中文正文、附录与后记，按章节整理为适合长文阅读的文档结构。
            </p>
          </div>

          <div class="flex flex-wrap gap-3">
            <UButton
              to="/docs"
              label="开始阅读"
              color="primary"
              variant="solid"
              trailing-icon="i-lucide-arrow-right"
            />
          </div>
        </div>

        <div class="grid gap-4 self-end">
          <UCard
            v-for="section in sections"
            :key="section.title"
            class="paper-panel rounded-[1.7rem]"
          >
            <div class="flex items-start justify-between gap-4">
              <div>
                <p class="text-sm uppercase tracking-[0.18em] text-dimmed">{{ section.title }}</p>
                <p class="mt-2 text-lg font-semibold text-highlighted">{{ section.description }}</p>
              </div>

              <UIcon :name="section.icon" class="mt-1 size-5 text-primary" />
            </div>
          </UCard>
        </div>
      </div>
    </section>

    <section class="page-surface rounded-[2rem] px-4 py-6 md:px-6">
      <div class="mb-6 flex flex-wrap items-end justify-between gap-4">
        <div>
          <p class="text-sm uppercase tracking-[0.2em] text-dimmed">目录</p>
          <h2 class="mt-2 text-3xl font-semibold text-highlighted">章节总览</h2>
        </div>

        <p class="max-w-xl text-sm leading-7 text-muted">
          可按顺序通读，也可以从感兴趣的主题直接进入。
        </p>
      </div>

      <div class="chapter-grid">
        <ChapterCard
          v-for="chapter in chapterMap"
          :key="chapter.id"
          :chapter="chapter"
        />
      </div>
    </section>
  </div>
</template>
