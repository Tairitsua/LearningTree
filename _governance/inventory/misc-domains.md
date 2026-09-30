# 盘点：小域与杂项（SoftwareManual/Fontend/English/Business/Koubot/Math/Music/README/templates，40 文件）

> 来源：治理阶段 A 探查子代理，2026-09-30。

## 一、逐文件记录

### SoftwareManual（16）

| 记录 |
|---|
| CMD.md \| 40.4KB \| 混 \| Windows CMD/PowerShell/注册表/批处理速查大全 \| H1多个(3)、①类标号(5处)、代码块无语言(6)、疑似过期(doskey 引 XP 版 technet 文档)、事实可疑(powercfg batteryreport 写法缺 `/` 参数) \| 与 Powershell.md 重叠(内含"## PowerShell"整章) |
| WSL.md \| 32.4KB \| 混 \| WSL+Kali+MyLinux(Docker)安装配置、代理、zshrc 全文、CTF 工具链 \| H1多个(3)、裸URL(12+)、代码块无语言(2)、疑似过期(整段 .zshrc 约420行全文粘贴，时效性差) \| 与 ComputerScience/Linux/Docker环境安装.md 重叠；"## Linux命令手册"与 Koubot/Linux命令.md 撞名；cryptohack/bkcrack 属 CTF 域 |
| VisualStudio.md \| 20.8KB \| 混 \| VS 编码/离线安装/插件/项目配置/发布/调试/快捷键 \| H1多个(6)、代码块无语言(10) \| SourceGenerator 与 Rider.md 重复；8 张 furion.net 外链图片(死链风险) |
| Clash.md \| 13.9KB \| 混 \| Clash 配置预处理(Parsers/Commands/JS 脚本)教程 \| 疑似过期(针对 Clash for Windows，官方 2023-11 已归档停更) \| 与 Proxifier.md、Microsoft.md 同属代理主题 |
| Git.md \| 9.9KB \| 混 \| Git 操作备忘(改历史/迁移/skip-worktree/.gitattributes/BFG/开源协议) \| 无(代码块内 `#` 注释非标题) \| — |
| MicosoftOffice.md \| 5.4KB \| 混 \| Office 通配符/Word/PPT/Excel 技巧 \| 命名拼写错误(MicosoftOffice) \| 无 |
| VSCode.md \| 3.5KB \| 混 \| VSCode vsix 导出/编码/快捷键 \| 无 \| "### HTML Emmet"与 HTML&CSS.md 重叠 |
| ReSharper.md \| 3.4KB \| 混 \| ReSharper 修复+File Layout+快捷键 \| 无 | 与 VisualStudio.md"### Resharper相关"重叠 |
| AHK.md \| 2.0KB \| 混 \| AutoHotkey v2 入门 | 无 | 无 |
| Proxifier.md \| 2.0KB \| en \| Proxifier fake DNS 断网排障(AI 回答粘贴,含 XML 证据) | AI 回答痕迹("Key evidence from your machine") | 与 Clash.md/Microsoft.md 同主题 |
| Typora.md \| 2.4KB \| zh \| Typora 自动标题编号 CSS 方案 | 无 | 与 README.md"## Typora"重叠 |
| Rider.md \| 2.3KB \| 混 \| Rider 换行/Keymap/主题/调试 SourceGenerator | 无 | SourceGenerator 与 VisualStudio.md 重复 |
| Powershell.md \| 1.0KB \| 混 \| PowerShell EncodedCommand+VBS 提权 | 无 | 手法偏安全域；与 CMD.md"## PowerShell"边界模糊 |
| Microsoft.md \| 0.4KB \| zh \| Microsoft Store 无法连接修复 | 空文件/极简；拼写"clsah" | 与 Clash/Proxifier 同主题；文件名过泛 |
| Acunetix.md \| 0.1KB \| zh \| 仅一句"忘管理员密码可改" | 空文件/极简 | 主题属安全域 |
| PowerToys.md \| 0.2KB \| zh \| 键盘映射去中文标点一句 | 空文件/极简 | 无 |

### Fontend（8；目录名拼写错误）

| 记录 |
|---|
| HTML&CSS.md \| 80.6KB \| 混(en为主) \| HTML/CSS 从零学习教程笔记 \| 仅 2 个 H2、H4 达 18 个，**全库最大文件未拆分** \| Emmet 与 VSCode.md 重叠 |
| Vue.md \| 14.7KB \| 混 \| Vue CLI/Vue2/Vue3 组件生命周期 | 无真实多 H1 | npm 命令与 TypeScript.md 重叠 |
| Blazor/Blazor.md \| 12.0KB \| 混 \| Blazor WASM/PWA/Integrity 大坑/调试/razor | 疑似过期(链接多 aspnetcore-6.0，已 EOL)；项目名"MyFontend"同拼错 \| 与 IsolationCSS.md 配对 |
| Javascript.md \| 12.2KB \| 混 \| JS 概念/ES 版本/DOM/语法糖/类型基础 | 疑似过期("目前2022年,主流浏览器都支持ES2017"时间锚) | Node 概念与 TypeScript.md"## Node"重叠 |
| FrontendConcept.md \| 5.6KB \| 混 \| CORS 原理(同源策略/简单复杂请求/CSRF) | 标题层级乱(深至H6) | 服务端 CORS 配置属后端域 |
| TypeScript.md \| 4.2KB \| 混 \| TS 配置报错+nvm/npm/Express 杂烩 | H2"问题"出现 2 次；内容混杂 | npm/nvm/Express 与 Javascript.md、Vue.md 互相重叠 |
| WebComponent.md \| 2.9KB \| 混 \| Web Component/Lit/Slot/ShadowDOM | 跑题(含"## Webpack"与"## 设计 Diagrams.net") | 设计工具节应归工具域 |
| Blazor/IsolationCSS.md \| 0.7KB \| zh \| Blazor CSS 隔离静态资源不更新排障 | 空文件/极简 | 是 Blazor.md"问题"章节候选 |

### 其余小域与根

| 记录 |
|---|
| English/English.md \| 31.4KB \| zh \| 英语语法体系(长难句/从句/短语/非谓语/句子成分/词性) \| 代码块无语言(59 个例句裸 ``` 块) \| 单文件承载全部语法，H2 仅 5 个 |
| Business/基础.md \| 3.8KB \| zh \| 恒生科技 ETF 联接基金 A/C 份额科普(AI 问答存档) \| 无H1、AI 对话残留("我可以帮你整理一份…需要吗？")、事实可疑(**"权重不会超过15%"——恒生科技指数个股上限实为 8%**)、文件名无信息量 \| 内容实为投资理财，与"Business"域名义不符 |
| Koubot/Linux命令.md \| 0.6KB \| 混 \| Linux 零散命令 3 条(按 LinuxShellPlugin 模板) \| H1多个(3 个模板条目各占 H1)、事实可疑("fc -l"是 POSIX shell 内建非 Linux 命令；"fc stands for fix command"为词典式解释) \| 应归 Linux 域；与 WSL.md"## Linux命令手册"重叠；Koubot 域仅此一文件 |
| Math/形式幂级数.md \| 1.7KB \| 混 \| 形式幂级数概念+代数"元/逆元" | 极简倾向 | 与 CTF crypto 隐式相关 |
| Math/数论.md \| 1.8KB \| zh \| 整除性质+同余/带余除法 | 标题层级乱(H2 下先 H4 再 H3) | 竞赛/密码学基础 |
| Music/MusicTheory.md \| 19.1KB \| zh \| 乐理:术语/认谱/调式音级/五度圈/钢琴 \| H1多个(5)、错别字"规化练习"、BPM "minutes"应为 minute \| "# 调（Scale）"与和弦.md 交叉 |
| Music/和弦.md \| 17.4KB \| zh \| 和弦体系(标记/家族/变化型/套路/织体/训练) \| H1多个(5) | "# 调式音阶"与 MusicTheory.md 直接重复 |
| Music/FLStudio.md \| 0.3KB \| zh \| FL Studio 快捷键 | 无H1、空文件/极简 | 无 |
| README.md \| 6.3KB \| 混 \| Markdown/Obsidian/Typora 使用配置+两条 AI 格式化/拆分提示词 | 定位失当(名为 README 实为工具笔记，无库导航) \| 与 Typora.md 重叠；AI 提示词属治理规范 |
| attachments/templates/（7 个） | 见下 | | | |

### attachments/templates（7）

1. **Csharp代码.md / Shell脚本.md / python脚本.md**：各为一个带语言标注的空代码块（```cs / ```sh / ```python）。
2. **LinuxShellPlugin.md**：Linux 命令条目模板——`# 功能名`+`## 命令`+`## 介绍`+`## 备注`。**模板每实例产生一个 H1，与"一文件一 H1"规范结构性冲突**（Koubot/Linux命令.md 即 3 实例堆叠致多 H1）。
3. **工具表.md**：三列表格（软件名/场景/备注）骨架，目前无文件使用。
4. **文件名.md**：CTF 题目命名规范 `{{date:YYYYMMDD}}_misc_隐写_小时_题目名`。
5. **正文.md**：CTF writeup 模板（题目名称/链接/描述/关键词/解题思路/详细过程）。

## 二、目录画像

- **SoftwareManual**：一软件一文件速查/备忘，模式最健康。例外：CMD/WSL/VisualStudio 三个巨型混合体。
- **Fontend**：教程型+备忘；目录名拼写错误是全库级问题（连 Blazor.md 项目样例都叫 MyFontend）。
- **English**：单文件 31KB 拆分候选。
- **Business**：域不副实（AI 问答存档、事实可疑）。
- **Koubot**：唯一文件与项目无关，放错域。
- **Math**：竞赛/密码学小抄，孤立无链接。
- **Music**：教程交叉（调式音阶两处）。
- **templates**：位于 attachments/ 内（被 userIgnoreFilters 隐藏，搜索不可见）。

## 三、笔记→笔记内部链接

**范围内 0 条。** 全部 63 条文本链接均为外部 URL/图片/同文件锚点（English.md 自身锚点×4、MusicTheory.md×1）。知识图谱完全无连接，重叠内容（SourceGenerator×2、Emmet×2、npm×3、调式音阶×2、代理排障×3）无互链。

## 四、图片引用

- 全部标准 `![](...)` 相对路径，无 wikilink 图片；42+ 张本地图片全部存在，无死链。
- 异常：VisualStudio.md 8 张 furion.net 远程图片（易失效）；Blazor 两文件用两级上跳；English.md 一图重复引用两次；大量 alt 为 Word 自动生成"描述已自动生成"。

## 五、>20KB 大文件拆分依据

- **HTML&CSS.md（80.6KB，607行）**：仅 2 个 H2（HTML/CSS），H3 11 个。先拆 HTML/CSS 两文件，再按 H3 二次拆。
- **CMD.md（40.4KB，857行）**：3 个 H1——# CMD（H2: PowerShell/Windows/设置Alias/文件操作/网络）、# 注册表、# 批处理基础（H2: 注释/输入与输出/标识符/IF/FOR）。按 H1 拆三文件，"## PowerShell"整章并入 Powershell.md。
- **WSL.md（32.4KB，845行）**：3 个 H1——# WSL（文件管理/命令/代理/问题）、# Kali（安装/Kex）、# MyLinux（Docker/常用包/自编译/Linux命令手册/zsh/Docker代理）。约 420 行 .zshrc 全文应抽出独立配置文件；Kali/CTF 工具与 CTF 域重叠。
- **English.md（31.4KB，806行）**：5 个 H2——长难句/从句/短语/句子成分/词性。按 H2 拆 5 文件。
- **VisualStudio.md（20.8KB，569行）**：6 个 H1（VS/项目配置/发布/模板/调试/快捷操作），每个 H1 下 H2 完整，标准 H1 拆分候选。

## 六、组织问题观察

1. 放错域：Koubot/Linux命令.md、Acunetix.md、WebComponent.md 内 Webpack/Diagrams.net 节、TypeScript.md 混杂内容。
2. 命名拼写：Fontend 目录、MicosoftOffice.md、MyFontend、Rider "Verison Control"、Proxifier "TroubleShotting"、MusicTheory "规化练习"、Microsoft "clsah"。
3. Linux 内容碎片化：Linux 域仅 1 文件，相关内容散在 WSL.md、Koubot、Git.md、Docker环境安装.md。
4. 小域合并选项：English/Business/Math/Music 保留充实 / 合并 Misc / Business 改名 Finance。Business 质量最低优先处理。
5. README 定位：根 README 无库导航；两条 AI 提示词是事实上的治理规范。
6. 链接网络缺失；极简文件 8 个；时效性问题多处（Clash 停更、aspnetcore-6.0 EOL、"目前2022年"、XP doskey 文档）。
