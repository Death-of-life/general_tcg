# 一般 TCG 理论文库

基于 Nuxt 4、@nuxt/ui、@nuxt/content 与 `nuxt-llms` 搭建的中文静态文档站，用来整理《一般 TCG 理论》的章节映射、中文精翻与 LLM 友好输出。

## 常用命令

```bash
pnpm install
pnpm dev
pnpm typecheck
pnpm build         # 等价于 nuxt generate，产出 .output/public
pnpm preview:static
pnpm preprocess:pdf
```

## 目录说明

- `content/docs/`：已发布的中文页面。
- `data/chapter-map.json`：章节映射的单一事实源。
- `data/terminology.json`：翻译、注释与 llms 共用的术语表。
- `scripts/preprocess_pdf.py`：内部预处理脚本，把 PDF 转成页级文本清单与章节源文件。
- `.baoyu-skills/baoyu-translate/EXTEND.md`：项目级翻译偏好。

## LLM 输出

- `/llms.txt`：结构化概览。
- `/llms-full.txt`：已发布内容的全文输出。
- `/raw/docs/*.md`：给模型抓取的原始 Markdown。

## Deploy on Cloudflare Pages (Git Integration)

参考 Cloudflare 官方文档：[Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)。

1. 在 Cloudflare Dashboard 打开 `Workers & Pages`，选择 `Create application`，然后 `Pages`。
2. 选择 `Connect to Git`，授权并选中本仓库与目标分支（如 `main`）。
3. 在构建配置中填写：
   - Build command: `pnpm generate`
   - Build output directory: `.output/public`
4. （可选）环境变量：
   - `NODE_VERSION=24`
   - `NUXT_PUBLIC_SITE_URL=https://<your-pages-domain>`
5. 点击 `Save and Deploy` 完成首次部署；后续向绑定分支 `push` 会自动触发 Pages 构建发布。
