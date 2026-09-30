# LearningTree 知识库规范（Agent 宪法）

> 本仓库是 **Obsidian 个人知识宫殿**（vault 根 = 仓库根）。本文件是所有 agent 与协作者在本仓库工作的唯一权威规范。
> 治理历史与审计记录见 `_governance/`（2026-09-30 完成首次全库治理，报告见 `_governance/REPORT.md`）。

## 1. 仓库定位与使用方式

- 用途：长期积累的个人知识库。典型入口是**知识入库**——用户丢来一条知识点/概念/经验，agent 按 §7 工作流自动归位。
- 结构：域（domain）→ 子域/主题 → 笔记。每个顶级域目录有 `README.md` 作为该域索引（MOC）。
- 工具链：Obsidian（标准 Markdown 相对链接、附件进 `attachments/`、模板在 `_templates/`、git 由 obsidian-git 自动备份）。

## 2. 域目录与边界规则

| 域 | 定位 | 备注 |
|---|---|---|
| `ComputerScience/` | 计算机科学原理与理论 | Algorithms、Linux、OperatingSystem、Network、Database、Architecture、Security、AI、BigData |
| `Programming/` | 编程语言与框架实践 | DotNet（语言层/Libraries/UI）、Cpp、Python、C、PHP、正则表达式、故障排查 |
| `Frontend/` | 前端 | HTML/CSS/JS/TS/Node 与 npm/Vue/WebComponent/CORS/Blazor |
| `CloudNative/` | 云原生 | Docker、Kubernetes、Dapr、Components、CICD、Deployments |
| `CTF/` | 攻防竞赛实战 | Crypto、Misc、Web、Reverse、Pwn、AWD、IncidentResponse、Toolbox、Hacker（个人项目） |
| `SoftwareManual/` | 软件使用手册与清单 | 一软件一文件；`软件清单.md` 为总清单 |
| `English/` `Math/` `Music/` `Finance/` | 通识/人文/理财学习 | 系列化课程文件 |
| `attachments/` | 图片与配置附件（平铺） | 引用一律相对路径 |
| `_templates/` | 模板 | 通用笔记、CTF writeup、Linux 命令条目等 |
| `_archive/` | 被取代的原稿（不删除，Obsidian 搜索已忽略） | 仅归档，不维护 |

**跨域边界**（拿不准时看这里）：
- **原理 vs 实战**：安全原理与防御 → `ComputerScience/Security/`；CTF 攻防技巧与工具 → `CTF/`。两侧互挂链接。
- **语言 vs 生态**：C#/F# 语言与 BCL → `Programming/DotNet/` 根；ASP.NET Core/EF Core/第三方库 → `DotNet/Libraries/`；.NET 相关云原生工具（Aspire 等）→ `Libraries/`（若偏部署则 `CloudNative/`）。
- **Blazor** 归 `Frontend/Blazor/`（前端框架视角）。
- **Linux 系统知识** → `ComputerScience/Linux/`；WSL/Kali 等本机环境 → `SoftwareManual/`。
- **正则表达式**等通用编程技能 → `Programming/`。
- 拿捏不准归属时：选最接近的既有文件并入；都没有则新建并更新域 README。

## 3. 命名规范

1. **目录名**：英文 PascalCase，禁止空格、括号、`+`（`Frontend`、`Kubernetes`、`Crypto`、`Cpp`）。
2. **笔记文件名**：中文主题词（`公钥密码密钥格式.md`）；英文专有名词保持英文原样（`Blazor.md`、`AsyncLocal.md`）；多词英文用连字符（`ASP.NET-Core-接口.md`）。
3. **系列课程文件**：两位序号前缀 `01-`、`02-`（`01-基本概念.md`）；速查/备忘/手册不加序号。
4. **CTF writeup**：`YYYYMMDD_分类_标签_时长_题目名`（模板见 `_templates/文件名.md` 与 `_templates/正文.md`）。
5. 文件名与 H1 标题保持一致。

## 4. 格式规范（每条笔记必须满足）

1. 文件标题作为**唯一 H1**；正文内不出现其他 H1；标题层级不跳级（H2 下不能直接 H4）。
2. 专有英文名词用反引号包裹（`Kubernetes`、`async/await`）。
3. 代码块必须带语言标注（`csharp`/`python`/`bash`/`yaml`/`text`…）；行内代码、命令、路径用反引号。
4. **保留作者原意**：仅修格式、语法、明确的事实错误；不做风格重写。
5. 不用 ①②③、全角（一）（二）、`※`、`•` 等非标准标号；一律 Markdown 有序列表/无序列表。
6. 裸外链 `<https://…>` 或纯文本 URL 改为 `[标题](URL)`。
7. 大段英文原文不翻译，仅调格式。
8. 空节要么补内容，要么写斜体*待补充：xxx*，不留空标题。
9. 表格内代码同样用反引号；外部权威来源优先引用官方文档。

## 5. 链接与附件

1. 只用**标准 Markdown 相对链接**（禁用 `[[wikilink]]`，Obsidian 已配置 `useMarkdownLinks: true`）。
2. 图片/附件一律放 `attachments/`，笔记内相对路径引用（`../attachments/x.png`，空格用 `%20`）。
3. 知识网络是硬要求：新增/修改笔记时，**更新所在域 README 索引**，并为主题相近的笔记补双向链接（"相关：[…]（…）"一行即可）。
4. 结构性改动（移动/改名/拆分文件）后必须运行：
   ```bash
   python _governance/scripts/fixlinks.py     # 重算相对链接
   python _governance/scripts/checklinks.py   # 校验，必须 all links OK
   ```
5. 禁止引入指向库外（`../../` 出 vault 根）的链接。

## 6. 内容政策

- **事实**：不确定的表述不要凭感觉改。加 `> [!question] 待事实核查：<疑点>` callout，联网查权威来源后再修；修正时留一行 `> YYYY-MM 核查修正：<旧> → <新>（来源）`。
- **时效**：含版本时点/停更/旧范式的笔记，文首加引用提示，如 `> 记录于 XXX 时期（YYYY-MM 官方归档），思想仍适用`。不删旧内容。
- **隐私红线**：明文密码、内网 IP、公司内部命名空间/Pod 名一律 `<已脱敏>` 替代，禁止入库。
- **归档与合并**：被拆分/重写的原稿移入 `_archive/<域>/`（文件名加`-原稿`后缀）；小文件被合并时内容并入目标后 `git rm`，并在 `_governance/migration-log-*.md` 或 commit message 留痕。任何信息删除必须在 git 历史与治理日志中可追溯。
- **转载**：保留来源标注（作者/链接/许可协议），标题降级到正文层级。

## 7. 知识入库工作流（核心场景）

用户丢来一条知识点（如"幂等性：f(f(x))=f(x)，分布式消息重复投递不产生副作用累积…"）时：

1. **判域**：读 §2 边界规则，确定归属域。
2. **判粒度**（关键决策）：
   - 小知识点（一个概念/一条命令/一个坑）→ **并入既有主题笔记**的相应小节（没有合适小节就新增一节，标题=知识点名）。
   - 大而独立的主题（成体系的知识）→ 新建笔记，文件名按 §3。
   - 一条命令 → `ComputerScience/Linux/01-命令速查.md` 等速查表加行；一个软件 → `SoftwareManual/` 对应文件或清单加行。
3. **写入**：按 §4 格式写；该知识点已有的重复表述先去重（保留更完整的版本）。
4. **织网**：更新域 README 索引；给 1-3 个相关笔记加"相关"互链。
5. **核查**：知识点中的事实性断言若可疑，按 §6 加 callout 或当场查证；与既有笔记矛盾的，以权威来源定对错。
6. **验收**：`python _governance/scripts/checklinks.py` → all links OK。
7. **提交**：`git add -A && git commit -m "knowledge: <主题一句话>"`（本仓库允许 agent 直接 commit；push 遵循用户当时的指示）。

示例（幂等性）→ 判域：分布式/后端概念 → 并入 `CloudNative/` 或 `Programming/DotNet/` 相关主题笔记（如消息/可靠性章节）；若无合适宿主，在 `CloudNative/` 下新建 `可靠性.md` 收纳并更新 README。

## 8. 治理工具与约定

- `_governance/scripts/`：`fixlinks.py`（链接重算）、`checklinks.py`（死链/孤儿图校验）、`lint_ctf.py`（结构 lint，可仿写用于其他域）。
- 结构 lint 标准：唯一 H1、无跳级、围栏闭合、围栏有语言。
- `_governance/`、`_archive/` 已加入 Obsidian `userIgnoreFilters`，不参与搜索。
- commit 约定：结构治理用 `governance:` 前缀，知识入库用 `knowledge:` 前缀，并写明要点。
