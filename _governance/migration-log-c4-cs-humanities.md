# 治理日志：C4 批（ComputerScience 域 + Math/Music/Finance 域格式扫尾）

> 执行日期：2026-09-30。范围：`ComputerScience/`（AI/Architecture/Algorithms/Linux/Database/BigData/Network/OperatingSystem/Security + 根级散文件）+ `Math/` + `Music/` + `Finance/`，共 58 个 md 文件的格式治理；另含 1 处域外门禁修复（`CloudNative/Components/Nginx.md` 链接深度，见 F0）。幂等原则：只修仍有问题的文件，本批未动的内容不再重复处理。未 `git commit`。
> 验收：`fixlinks.py` → `DONE: 0 links fixed`；`checklinks.py` → `all links OK`（245 md 文件；31 张 orphan 图片为其他域历史存量，与本批无关，未动）。全量 lint（唯一 H1 / 无跳级 / 围栏闭合 / 围栏语言）扫描本批全部文件，修复后 CLEAN。

## A. ComputerScience/AI（4 篇）

| 操作 | 对象 | 说明 |
|---|---|---|
| 重写 | `AI/LLM安全-提示注入与越狱.md` | 原文为两段整段粘贴的 AI 对话（无任何标题、含"刚才遇到的""我上一轮拒掉""是的，你描述的""下面拆开讲""讲点反方的，免得你觉得""想深入的话"等对话痕迹）。重写为结构化笔记：唯一 H1 `# LLM 安全：提示注入与越狱`，分节：常见攻击手法（老套类）/ 更巧妙的攻击手法 / 上下文伪造类攻击（agent 场景）/ 为什么有效——底层机制 / 一般性规律 / 研究现状 / 攻击的真实上限 / 防御措施。全部知识点保留，删除对话性语句（含对话专属指代"把反作弊脚本打磨得更隐蔽"，泛化为"核心有害动作不会变"），专有英文名词补反引号，文件头部加 `[!note]` 整理说明留痕。 |
| 拼写修正 | `AI/神经网络入门.md` | `tf.random.unifrom` → `tf.random.uniform`（两处拼写笔误合一：`unifrom`→`uniform`）。 |
| H1 修正 | `AI/神经网络入门.md` | H1 `# 人工智能` → `# 神经网络入门`（与文件名一致；文中本有 `## 神经网络设计过程` 等主体内容）。 |
| H1 修正 + 时效注 | `AI/Roop换脸环境.md` | H1 `# 图像处理` → `# Roop换脸环境`（文件内容仅 Roop，与文件名一致）；文首加 `> 记录于 CUDA 11.8 时期，新版依赖可能不同`。 |
| H1 修正 | `AI/人声分离UVR5.md` | H1 `# 音频处理` → `# UVR5 人声伴奏分离`（与文件名一致）。 |

## B. ComputerScience/Architecture（8 篇）

| 操作 | 对象 | 说明 |
|---|---|---|
| 空节处理 | `Architecture/ABP.md` `## Time （UTC与本地时间）` | 原为文末空章节。未删除，补一段"待补充"标注：ABP 中统一通过 `IClock`（`Clock.Now`）获取当前时间，返回 UTC 还是本地时间由 `AbpClockOptions.Kind`（`Unspecified`/`Local`/`Utc`，默认 `Unspecified`）决定，设为 `Utc` 后 `Clock.Now` 返回 UTC 时间；入库/出库转换细节待补充。 |
| 代码块语言 | `Architecture/ABP.md` | "注册问题"节 `The requested service 'Volo.Abp.DependencyInjection.ObjectAccessor…'` 报错代码块补 `text`。 |
| 快速核查 | 其余 7 篇（DDD基础/README/交付流程与软件工程/微服务与分布式架构/架构基础与设计原则/架构模式与UML/设计模式/限界上下文与领域模型） | lint 通过：唯一 H1、无跳级、围栏闭合且带语言。零改动。 |

## C. ComputerScience 其余目录（快速核查）

| 操作 | 对象 | 说明 |
|---|---|---|
| 回归确认 | `Algorithms/`（7 篇） | 此前批次的"有序树定义写反"修正注与"快速幂独立成节"修正注均在位；lint 通过，无回归。`03-树.md` 存在两个 `## 性质`（树的性质 / 二叉树的性质），分属不同父节，不违反规范，保留。 |
| H1 修正 + 代码块语言 | `Database/数据库基础.md` | H1 `# 数据库` → `# 数据库基础`（与文件名一致，避免与内部 `## 数据库基础` 节混淆层级语义）；"索引"节两个数据示例代码块补 `text`。 |
| 快速核查 | `Database/MySQL.md`、`Database/SQLServer.md`、`Database/README.md` | lint 通过，零改动。`SQLServer.md` H1 `# SQL Server` 与文件名仅差一个空格（展示惯例），保留。 |
| 快速核查 | `BigData/`（3 篇） | lint 通过，零改动。`Hadoop生态.md` H1 `# 大数据与 Hadoop 生态` 为描述性标题，保留。 |
| 快速核查 | `Linux/`（8 篇） | lint 通过，零改动。`06-SSH.md` 第 33 行 `#StrictModes yes` 为代码块内配置注释，非标题，勿误判。`01-命令速查.md` H1 `# Linux 命令速查`、`03-Shell脚本.md` H1 `# Shell` 为编号前缀剥离后的既定命名风格，保留。 |
| 快速核查 | `Network/计算机网络.md` | lint 通过（此前并入 WEB.md 内容后结构完好），零改动。 |
| 幂等确认 | `OperatingSystem/操作系统.md` | 已有唯一 H1 `# 操作系统`（种子文件，含信号量/文件系统两节），无需补，零改动。 |
| 快速核查 | `Security/`（7 篇） | lint 通过，README 目录链接经 checklinks 验证有效，零改动。 |

## D. ComputerScience 根级散文件

| 操作 | 对象 | 说明 |
|---|---|---|
| 时效注 | `SoftwareTest.md` | 文首加 `> 引自 2020 年面试题博客，注意时效`。 |
| H1 格式 | `Unity.md` | H1 `` # `Unity` `` 去反引号 → `# Unity`（标题不携带代码格式）。 |
| 幂等确认 | `IoT.md` | 唯一 H1 `# 物联网` 在位，重复句已于此前的治理中移除，零改动。 |

## E. Math（2 篇）

| 操作 | 对象 | 说明 |
|---|---|---|
| 层级归位 | `Math/数论.md` | `## 整除` 下 `#### 单项式上横线表示位数而不是单项式` 上调为 H3，消除 H2→H4 跳级，与后续 `### 性质` 归位同级。H1 `# 数论` 原本在位，无需补。 |
| H1 修正 | `Math/形式幂级数.md` | 补唯一 H1 `# 形式幂级数`；原 `# 概念` 降为 H2，`## 元的概念`→H3、`### 逆元素（Inverse element）`→H4，整体层级顺移一级，无跳级。 |
| 互链 | `数论.md`、`形式幂级数.md` 文末 | 各加一行 `相关：[RSA与数论](../CTF/Crypto/RSA与数论.md)`。注意：任务清单原文写作 `../../CTF/...`，从 `Math/` 出发实际只需一级 `../`（两级会逃出 vault 根），已按正确相对路径写入并经 checklinks 验证。 |

## F. Music（3 篇）

| 操作 | 对象 | 说明 |
|---|---|---|
| H1 降级重构 | `Music/MusicTheory.md` | 5 个 H1 → 唯一 H1 `# 乐理`；`术语`/`认谱`/`规划练习`/`调（Scale）`/`钢琴` 降为 H2。子层级相应归位：认谱下 10 个 H4 谱号/认谱法小节 → H3；调（Scale）下 `快速认出五线谱调号`/`首调唱名法`/`音的稳定性与倾向性` H5 → H3；钢琴下 `钢琴踏板`→H3、三个踏板小节→H4、`细节`→H5、`共振`→H6、`建议`→H5。 |
| 错别字 | `Music/MusicTheory.md` | `# 规化练习` → `规划练习`（规化→规划）。 |
| 拼写修正 | `Music/MusicTheory.md` | `BPM beats per minutes` → `beats per minute`。 |
| 互链 | `Music/MusicTheory.md` 文首 | 加 `> 相关和弦知识见 [和弦](和弦.md)。`（`调（Scale）` 节与 和弦.md `调式音阶` 节内容交叉，按任务要求各自保留、文首互链）。 |
| H1 降级重构 | `Music/和弦.md` | 5 个 H1 → 唯一 H1 `# 和弦`（原 `# 和弦 (Chord)` 同步去掉英文尾注）；`调式音阶`/`和弦套路`/`伴奏织体`/`训练方式` 降为 H2，子层级整体顺移：`五度循环圈`/`自然小调`/`关系大小调`/`和弦色彩`/`和弦功能`/`织体`/`节奏型`→H3，`记忆方式`→H4；`三和弦(Triad)、七和弦…` 节下 9 个 H4（概念/大三/小三/减三/大七/大小七/小七/半减七）→ H3 消除跳级；`训练方式` 下 `1+3配置` H4→H3。 |
| 互链 | `Music/和弦.md` 文首 | 加 `> 相关乐理基础见 [MusicTheory](MusicTheory.md)。`。 |
| H1 补充 | `Music/FLStudio.md` | 补唯一 H1 `# FL Studio`。 |

## G. Finance（1 篇）

| 操作 | 对象 | 说明 |
|---|---|---|
| H1 补充 + 层级 | `Finance/恒生科技ETF联接基金.md` | 补唯一 H1 `# 恒生科技 ETF 联接基金`；原 `### 一、/二、/三、` 三节升为 H2（消除 H1→H3 跳级），"一、二、三"中文序号为标题组成部分，非 ①②③ 行内标号，保留。 |
| AI 对话残留删除 | 同上 | 删除结尾对话句"我可以帮你整理一份**易方达和博时恒生科技ETF联接C的费率对比表**…需要吗？"；删除开头"对于新手来说""下面用通俗的语言拆解所有问题"对话导语（保留核心论点句）；两处"你朋友说 C 好"中性化为"常见的'C比A好'说法"/"说 C 好"（指代信息不丢）。 |
| 待核查 callout | 同上 | "权重不会超过15%"原文未改，其后加 `> [!question] 待事实核查：恒生科技指数单只成分股权重上限疑似为 8%，15% 待确认`。 |

## F0. 域外门禁修复（非本批范围，为通过 checklinks 所需）

| 操作 | 对象 | 说明 |
|---|---|---|
| 链接深度修正 | `CloudNative/Components/Nginx.md:12` | CloudNative 批工作区新增的"相关条目"链接 `../../Kubernetes/故障排查.md` 指向 vault 根（不存在），目标实为 `CloudNative/Kubernetes/故障排查.md`（已核实该文件含链接描述的"Nginx 消息截断""获取用户真实 IP"两条记录），修正为 `../Kubernetes/故障排查.md`。 |

## 全量扫描结论（修复后）

- 唯一 H1：58/58 文件各恰有 1 个 H1（README.md 索引文件按库内既定惯例使用目录主题名作 H1，如 `# 架构`/`# Linux`/`# BigData`，非文件名，视为约定保留）。
- 标题跳级：0 处。
- 围栏：全部闭合；无语言代码块 0 处（本批修复 3 处：ABP.md ×1、数据库基础.md ×2）。
- ①②③类标号：全量扫描 0 处。
- 裸外链：正文无裸 URL；残留 http(s) 字符串均位于代码块或命令表格内（命令内容，非链接，rule 6 不适用）。

## 新增待核查 callout 清单（阶段 D 联网核实）

1. `Finance/恒生科技ETF联接基金.md`：恒生科技指数单只成分股权重上限疑似为 8%，原文"权重不会超过15%"待确认。
2. `ComputerScience/Architecture/ABP.md`：`Time` 节为"待补充"标注——`AbpClockOptions.Kind` 默认值（`Unspecified`）及设为 `Utc` 后 `Clock.Now` 行为、实体入库/出库转换细节待官方文档核实。
