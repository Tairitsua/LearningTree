# ComputerScience 域治理日志（阶段C3：拆分/合并/归位）

日期：2026-09-30。执行代理：知识库治理执行代理（ComputerScience 域）。
前置：阶段C1 目录重组已完成。全程使用 `git mv`/`git rm` 保留历史，未 commit（由主控统一提交）。

## T1 Linux.md（208KB 巨石）→ ComputerScience/Linux/

拆分脚本：`_governance/scripts/c3_split_linux.py`（按标题边界机械切分，跳过代码围栏内 `#` 行）。

| 操作 | 对象 | 去向/说明 |
| --- | --- | --- |
| 拆分 | `# 命令` 章主体命令表 + `## 快捷键` + `## 运行级别runlevel` | `Linux/01-命令速查.md`（H1 `# Linux 命令速查`） |
| 拆分 | `## Vim` | `Linux/02-Vim.md`（H1 `# Vim`） |
| 拆分 | `# Shell` 章简介 + `## Shell脚本` + `## 目录结构` + `## 种类` | `Linux/03-Shell脚本.md`（H1 `# Shell`，章简介保留为文件引言） |
| 拆分 | `# Shell` 下错挂的 `## 文件权限`、`## 用户`、`## 组` | `Linux/04-用户与权限.md`（H1 `# 用户与权限`） |
| 拆分 | `## 进程` + `# 硬盘管理` | `Linux/05-进程与磁盘.md`（H1 `# 进程与磁盘`） |
| 拆分 | `# SSH` | `Linux/06-SSH.md`（H1 `# SSH`） |
| 拆分 | `# 网络设置` | `Linux/07-网络配置.md`（H1 `# 网络配置`，有意改名对应文件名） |
| 归档 | `ComputerScience/Linux.md` | `git mv` → `_archive/ComputerScience/Linux-原稿.md`，开头加"> 本原稿已拆分至 ComputerScience/Linux/" |
| 新建 | `Linux/README.md` | 索引：各文件一句话简介 + 阅读顺序 |
| 并入 | `Koubot/Linux命令.md`（3 条目：os-release / fc -l / 学习资源链接） | `Linux/01-命令速查.md` 末尾"命令补遗"节；原 `## 介绍`、`## 备注` 空占位节清理（留痕于该节引言）；随后 `git rm`，`Koubot/` 目录已空随删 |
| 待并入 | 原稿 `# WSL` 章 → `SoftwareManual/WSL.md` | **跳过**：检查时 `SoftwareManual/WSL.md` 仍为未拆分原稿（另一代理拆分中），按预案不动；且该章实际仅含一行跳转链接 `[WSL](../SoftwareManual/WSL.md)`，无正文可并入，无信息损失 |

顺手修复（盘点发现，均留痕于脚本输出）：

1. wc 命令重复两行：删除第二行（`| wc | | 统计文件 |`），保留含 `word count` 全称的首行。
2. 原稿 L246 孤立字符 `f`（`## 快捷键` 表后）：删除。
3. 表格内裸 URL 2 处：jianshu（xargs 行）、zhihu（tcpdump 行）改 `[描述-来源](URL)`；SSH 章 cnblogs 裸链接同理。
4. 标题跳级修复：`#### 变量`→`### 变量`、`#### 特殊权限`→`### 特殊权限`、`##### 出现莫名奇妙无法连接…`→`##`；SSH/网络设置/用户章散落命令行补 ```shell/```ini 代码围栏；`1、`式序号改 Markdown 列表序号。
5. 全部产物唯一 H1；图片相对路径经 `fixlinks.py` 重算（`../attachments` → `../../attachments`）。

## T2 Database.md（43KB）→ ComputerScience/Database/

拆分脚本：`_governance/scripts/c3_split_database.py`（含标题层级栈归一）。

| 操作 | 对象 | 去向/说明 |
| --- | --- | --- |
| 拆分 | `# 数据库`（`## 基础知识` + `## 数据库基础` 两个 H2 合并整理） | `Database/数据库基础.md`（H1 `# 数据库`） |
| 并入 | `# DBF`（仅 3 行警告） | `数据库基础.md` 末尾 `## DBF` 小节 |
| 拆分 | `# SQL Server` | `Database/SQLServer.md`（H1 `# SQL Server`） |
| 拆分 | `# MySQL` | `Database/MySQL.md`（H1 `# MySQL`） |
| 归档 | `ComputerScience/Database.md` | `git mv` → `_archive/ComputerScience/Database-原稿.md`，加已拆分说明 |
| 新建 | `Database/README.md` | 索引：阅读顺序 + 各篇主题 |

格式修复：10 处标题跳级归一（如 `##### := 符号`→`####`、`#### Navicate 无法连接`→`###` 等）；MySQL 字符编码小节 3 个标题语义性摆正（`修改数据库的字符集及字符编码`、`使用Mysql数据库函数解码…` 提为 `###` 与 `utf8mb4_0900_ai_ci` 并列，保留原相对层级）。

## T3 BigData.md（36KB）→ ComputerScience/BigData/

拆分脚本：`_governance/scripts/c3_split_bigdata.py`。

| 操作 | 对象 | 去向/说明 |
| --- | --- | --- |
| 拆分 | `## 概念` + `## Hadoop框架` | `BigData/Hadoop生态.md`（H1 `# 大数据与 Hadoop 生态`） |
| 拆分 | `## 云数据中心` | `BigData/云数据中心.md`（H1 `# 云数据中心`） |
| 归档 | `ComputerScience/BigData.md` | `git mv` → `_archive/ComputerScience/BigData-原稿.md`，加已拆分说明 |
| 新建 | `BigData/README.md` | 索引：阅读顺序 + 各篇主题 |

## T4 Algorithms 重编号

| 操作 | 对象 | 去向/说明 |
| --- | --- | --- |
| 并入 | `01-附录.md`（引用符&/取整符号[]/C语言） | `02-基本概念.md` 末尾 `## 附录` 小节（内部 H2 降 H3）；随后 `git rm 01-附录.md` |
| 重命名 | 02-基本概念→01-基本概念、03-线性表→02-线性表、04-树→03-树、05-图→04-图、06-查找→05-查找、07-排序→06-排序、代码优化.md→07-代码优化.md | 全部 `git mv`，编号连续；改名前已确认库内无入站链接 |
| 新建 | `Algorithms/README.md` | 索引：阅读顺序 + 各篇主题（摘要按各篇实际 H2 校对） |
| 修复 | `03-树.md`（原 04-树）有序树/无序树定义写反 | **确认属实**（原文与二叉树"有左右之分，是有序树"自相矛盾），交换定义并加引用块留痕 |
| 修复 | `07-代码优化.md`（原 代码优化.md）快速幂挂在"浮点运算优化"下 | 独立为同级 `## 快速幂算法`；"浮点运算优化"原无独立内容，空标题移除，均留痕 |

## T5 收尾归位

| 操作 | 对象 | 去向/说明 |
| --- | --- | --- |
| 并入 | `ComputerScience/WEB.md`（WWW/域名、正反向代理 3 条） | `Network/计算机网络.md` `## 应用层（第七层）` 下新增 `### WWW 与域名`、`### 正向代理和反向代理` 两小节，注明来源；`git rm WEB.md` |
| 检查 | `ComputerScience/Architecture/README.md` | 内容与扁平化现状一致（8 文件均存在）；补充 ABP.md 导航行与阅读顺序提示 |
| 修复 | `ComputerScience/IoT.md` 首段 | "感知层是物联网的核心，是信息采集的关键部分"重复两次，删除句尾重复 |

## 门禁结果

1. `python _governance/scripts/fixlinks.py` → 拆分产物及归档稿图片/笔记链接全部重算；`python _governance/scripts/checklinks.py` → **all links OK**（248 md 扫描；孤儿图片不计失败）。
2. 标题覆盖核对：`_governance/scripts/c3_verify_split.py` → **ALL HEADINGS COVERED**（三份原稿全部 H1–H6 标题在产物中命中；唯一差异 `网络设置`→`网络配置` 为任务书指定的有意改名）。
3. 本日志即第 3 项门禁。

## 遗留/新发现

- `SoftwareManual/WSL.md` 拆分（另一代理）完成后无需回补：Linux 原稿 WSL 章仅一行跳转链接，无正文。
- 治理中未新增孤儿图片；31 个孤儿图片系其他域历史遗留，未动。
- 规范冲突取舍：规则 2（专有名词反引号）与规则 4（尽量不改内容）在大体量旧稿上冲突，本次仅对新增标题/README/引言与顺手修复的行应用反引号，未对旧正文做全量术语包裹，避免大面积无信息 diff。
