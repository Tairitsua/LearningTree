# 治理日志：Frontend / English 批（C2）

> 执行日期：2026-09-30。范围：`Frontend/`、`English/` 两域内容操作（拆分/合并/格式治理）。
> 原则：不丢信息、`git mv`/`git rm` 保留历史、内容改动留痕于本文件。原稿归档均保留原文（含原有格式瑕疵），仅追加说明。

## T1 `Frontend/HTML&CSS.md`（81KB，全库最大）拆分

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 拆分 | `Frontend/HTML&CSS.md` | 按现有 2 个 H2 拆为 `Frontend/HTML.md`（H1 `# HTML (Hyper Text Markup Language)`）与 `Frontend/CSS.md`（H1 `# CSS (Cascading Style Sheet)`）；原 H2 即文件标题，内部 H3/H4/H5/H6 依次提升为 H2/H3/H4/H5，无跳级。两半之间无跨域引言/总结，无需搬运。`Table beautify` 空节保留（原文如此）。 |
| 归档 | `Frontend/HTML&CSS.md` | `git mv` → `_archive/Frontend/HTML与CSS-原稿.md`，文首加"已拆分归档"说明。 |
| 格式核查 | HTML.md / CSS.md | 代码块原已全部带语言标注（`html`/`css`），无 ① 类标号，未做内容改动。 |

## T2 Frontend 内容收敛

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 抽出 | `Frontend/TypeScript.md` 的 `## Node`、`## npm`、`## Express` 及文末第二个 `## 问题`（`Cannot find module 'supports-color'`） | 移入新建 `Frontend/Node与npm.md`；`TypeScript.md` 保留 TS 配置报错（`tsconfig.json` 的 `lib`/`esModuleInterop` 等），文首留链接句指向 `Node与npm.md`。 |
| 合并 | `Frontend/Javascript.md` 的 `## 概念` Node 概念段（`Node.js` 运行时类比 `JVM`/`CLR`、`Server-Side` 执行、与 `Vue.js`/`React`/`Angular` 区别、原 `### 框架` 节的 `v8`/`libuv`/第三方模块） | 原文整体移入 `Node与npm.md` `## Node` 节；`Javascript.md` 原处缩为一句概括+链接（`### 框架` 标题随之移除；`TypeScript` 中间语言段与 `Javascript.md` 主题相关，保留原地）。 |
| 合并 | `Frontend/Vue.md` 的 npm 命令（`Vue CLI` 节） | 通用 `npm` 知识（`-g`/`-S`/`-D`、`dependencies` 等）已汇总于 `Node与npm.md`；`Vue.md` 在 `## Vue CLI` 节首加链接行。与 `Node与npm.md` 重复的 `npm install -g @vue/cli` 一行保留于 Vue CLI 工作流上下文中（删除会破坏工作流完整性），`serve -s dist` 本地预览为 Vue 专属内容，保留。 |
| 并入 | `Frontend/Blazor/IsolationCSS.md`（0.7KB 排障） | 内容并入 `Frontend/Blazor/Blazor.md` `## 问题` 节新增 `### CSS 隔离（Isolation CSS）打包与更新问题`（原文保留），随后 `git rm`。 |
| 加注 | `Frontend/Blazor/Blazor.md` | 文首加时效提示：链接基于 `ASP.NET Core 6.0`（2024-11 EOL），概念仍适用。 |
| 不动 | `Blazor.md` 中 `MyFontend.*` 项目名 | 用户真实项目目录名（拼写虽似 Frontend），保留不改。 |
| 移出 | `Frontend/WebComponent.md` 原 `## 设计`/`### Diagrams.net` 节（离题） | 详细内容（一句话简介 + diagrams.net 官网链接 + 添加图标教程链接）移入 `Frontend/README.md` "相关工具"行；`WebComponent.md` 原处删除并留 blockquote 说明。`## Webpack` 节为前端构建相关，保留原地。 |
| 修正 | `Frontend/Javascript.md` 时效表述 | "目前2022年,主流浏览器都支持ES 2017所有特性。所以可以放心用。" → "截至 2022 年，主流浏览器已支持 `ES2017` 所有特性，可以放心用。" |
| 格式 | `Frontend/CORS.md` | 原 H1 `# Frontend Concept` 退役（文件已于 C1 改名 CORS.md，题文不符）；原 H2 `CORS(Cross-Origin Resource Sharing) 跨站资源共享` 提升为 H1，其余标题各提升一级，消除全部 H6（原最深 H6 定义/流程 → H5）；清理标题行尾空格。正文内容零改动。 |
| 格式 | `Frontend/Vue.md` | 核查通过：唯一 H1、无跳级、代码块均带语言（`bash`/`javascript`/`html`/`vue`）、专名反引号，仅新增 Node与npm.md 链接行。 |
| 格式 | `Frontend/HTML.md`、`Frontend/CSS.md` | 见 T1。 |

## T3 `English/English.md`（31KB，5 个 H2）拆分

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 拆分 | `English/English.md` | → `01-长难句解析.md`（H1 词序由"解析长难句"调整为"长难句解析"，与文件名一致）、`02-从句.md`（H1 保留原标题 `从句（Subordinate/dependent Clause）`）、`03-短语与非谓语.md`（H1 由"短语"扩为"短语与非谓语"以涵盖非谓语动词/复合结构内容）、`04-句子成分.md`、`05-词性.md`。各 H2→H1，内部标题提升一级，无跳级。 |
| 格式 | 59 个例句裸代码块 | 全部补 `text` 语言标注。 |
| 锚点 | `[非谓语动词](#非谓语动词又名nonfinite-verb-非限定动词的一般结构)` ×3（01 内） | 改为跨文件相对链接 `03-短语与非谓语.md#非谓语动词又名...`（已人工核对目标标题 slug 一致）。`03` 内自锚点 `[动名词的复合结构](#动名词复合结构)` 目标仍在本文件，保留。 |
| 规整 | `02-从句.md` 3 个越级标题 | 原 `##### 从句并列`、`##### 状语从句的省略`、`##### 让步状语从句` 为作者笔误性深层级（提升后会造成跳级），分别规整为 `##`/`###`/`###`。 |
| 去重 | 图片 `attachments/13ef9069….png`（原稿引用两次，均在长难句部分） | 保留"找介词"节带解说处（"这里的一连串介词分隔开真正的主谓老远"），删除"从属连词"节无解说的一处；原稿归档件中两处均保留。 |
| 新建 | `English/README.md` | 5 篇索引（篇目+一句话内容）+ 原稿归档链接。 |
| 归档 | `English/English.md` | `git mv` → `_archive/English/English-原稿.md`，文首加"已拆分归档"说明。 |

## T4 域索引

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 新建 | `Frontend/README.md` | 9 篇笔记导航（HTML/CSS/Javascript/TypeScript/Node与npm/Vue/WebComponent/CORS/Blazor，各一句话）、"相关工具"（Diagrams.net，自 WebComponent.md 移入）、跨域互链建议（`Programming/DotNet/Libraries/ASP.NET-Core.md`、`CloudNative/CloudNative.md`）。 |

## 验收记录

- `python _governance/scripts/fixlinks.py`：首轮修复 25 条链接（全部为两份归档原稿的 `../attachments/` 深度重算为 `../../attachments/`，其余文件链接原已正确）；复跑 0 修复（幂等确认）。
- `python _governance/scripts/checklinks.py`：**`all links OK`（退出码 0，232 个 md 文件）**。首轮曾报 CTF/Crypto 两处指向 `编码速查.md` 的 DEAD 链接（CTF 批代理 in-flight 产物，非本批引入），验收复跑时目标文件已由该批建出，死链消失。
- 31 张孤儿图为存量（git HEAD 即无任何引用，与本批无关），留待 F 阶段统一隔离。
- 标题结构审计：本批全部活跃文件唯一 H1、无层级跳跃、代码块全部带语言标注；两份归档原稿按"保留原文"原则未整改其原有格式瑕疵。
- 未 commit（按任务要求，交由上层统一提交）。
