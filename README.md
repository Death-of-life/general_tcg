# 一般 TCG 理论文库

基于 Nuxt 4、@nuxt/ui、@nuxt/content 与 `nuxt-llms` 搭建的中文静态文档站，用来整理《一般 TCG 理论》的章节映射、中文精翻与 LLM 友好输出。

[![Deploy on Cloudflare Pages](https://img.shields.io/badge/Deploy%20on-Cloudflare%20Pages-F38020?logo=cloudflare&logoColor=white)](https://developers.cloudflare.com/pages/get-started/git-integration/)
[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/Death-of-life/general_tcg)

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

说明：Cloudflare 官方的 `Deploy to Cloudflare` 一键部署按钮目前仅支持 Workers，不支持 Pages（见官方 Deploy Buttons 文档的 Limitations）。

1. 在 Cloudflare Dashboard 打开 `Workers & Pages`，选择 `Create application`，然后 `Pages`。
2. 选择 `Connect to Git`，授权并选中本仓库与目标分支（如 `main`）。
3. 在构建配置中填写：
   - Build command: `pnpm generate`
   - Build output directory: `.output/public`
4. （可选）环境变量：
   - `NODE_VERSION=24`
   - `NUXT_PUBLIC_SITE_URL=https://<your-pages-domain>`
5. 点击 `Save and Deploy` 完成首次部署；后续向绑定分支 `push` 会自动触发 Pages 构建发布。

## Deploy to Cloudflare Workers (One-click Button)

参考 Cloudflare 官方发布说明：[Deploy to Cloudflare button](https://developers.cloudflare.com/changelog/post/2025-04-08-deploy-to-cloudflare-button/)。

1. 点击 README 顶部的 `Deploy to Cloudflare Workers` 按钮。
2. 在 Cloudflare 页面授权后，系统会基于此仓库创建你自己的副本仓库并引导部署。
3. 按提示完成构建配置（静态站可使用 `pnpm generate`，输出目录 `.output/public`）。
4. 完成后，后续对新仓库分支的推送可触发自动构建与部署（由 Workers Builds 管理）。

> 注意：该按钮是 Workers 路线，不等价于 Pages Git Integration。若你要保留当前 Pages 工作流，请继续使用上面的 Pages 章节。
