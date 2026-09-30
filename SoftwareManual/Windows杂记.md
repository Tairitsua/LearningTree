# Windows 杂记

> 治理留痕（2026-09-30）：本文件由原 `SoftwareManual/Microsoft.md` 与 `SoftwareManual/PowerToys.md` 两个极简文件合并而来（`git rm` 原文件），拼写错误"clsah"已修正为 `Clash`。

## Microsoft Store 连接问题

商店无法连接问题解决方案：

用Clash挂代理的话，开UWP应用网络回环，选中Microsoft Store等UWP应用再连接就正常了

Internet Options中 Advanced里面勾选 TLS1.0 到 TLS1.3，Connections中LAN Setting里面将 Proxy server里面Use a proxy server for your LAN (These settings will not apply to dial-up or VPN connections).去掉。 并勾上Automatically detect settings

## PowerToys 键位映射

这个可以把根本不用的中文标点符号给弄掉了，比如`` ` ``这个标点符号映射成文本即可。
