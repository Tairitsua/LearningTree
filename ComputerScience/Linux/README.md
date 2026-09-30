# Linux

原巨石笔记 `ComputerScience/Linux.md`（约 200KB）已于 2026-09-30 阶段C3 拆分为本目录下的独立笔记；原稿归档于 `_archive/ComputerScience/Linux-原稿.md`。

## 阅读顺序与简介

建议按编号顺序阅读，入门可先看 01/02，做系统管理再读 04/05/07：

1. [01-命令速查](01-命令速查.md)——常用命令大表（文件操作、用户、进程、软件包、压缩、网络、磁盘分区），附终端快捷键、运行级别（runlevel）与命令补遗。
2. [02-Vim](02-Vim.md)——`vi`/`vim` 的三种模式与移动、删除复制粘贴、查找替换、分屏等命令表。
3. [03-Shell脚本](03-Shell脚本.md)——`Shell` 是什么、`.sh` 脚本语法（变量、字符串、数组、调试选项）、Linux 目录结构与 `Shell` 种类。
4. [04-用户与权限](04-用户与权限.md)——`rwx` 权限与特殊权限（SUID/Sticky）、用户与组管理（`/etc/passwd`、`/etc/shadow`）、`sudo` 授权与配置文件加载顺序。
5. [05-进程与磁盘](05-进程与磁盘.md)——进程概念、分类与属性；硬盘主分区/扩展分区/逻辑分区的划分规则。
6. [06-SSH](06-SSH.md)——SSH 免密登录失败的两类排查（权限、`StrictModes`）。
7. [07-网络配置](07-网络配置.md)——`ifcfg` 网卡配置、`nmtui`、VMware 桥接模式与 SELinux 端口问题排查。

WSL 相关内容见 [SoftwareManual/WSL](../../SoftwareManual/WSL.md)。
