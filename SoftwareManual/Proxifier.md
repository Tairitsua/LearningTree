# Proxifier

> 治理留痕（2026-09-30）：本文件原为 AI 排障回答的直接粘贴（含"Key evidence from your machine""I hope that helps"等口吻），已重写为中性笔记语气；全部技术信息（含 XML 配置证据）原样保留，仅调整叙述结构。

## Troubleshooting

### 部分程序无法连接网络、DNS 解析失败

> 治理留痕（2026-09-30）：原标题 "TroubleShotting" 拼写已修正为 "Troubleshooting"。

现象：一部分程序无法连接网络，DNS 解析失败。

排查结论：不是 Tailscale DNS 的问题，根本原因是 Proxifier 的 fake DNS / remote DNS 模式泄漏到了 direct（直连）连接。

本机排查时的关键证据：

- `rawchat.cn` 解析为 `127.170.10.30`
- `drive.weixin.qq.com` 解析为 `127.170.10.88`
- Windows DNS 缓存中存在大量 `127.170.10.x` 记录，且 TTL 极长
- AAAA 记录形如 `fd00:696e:6974:6578::...`，其中 `696e:6974:6578` 十六进制解码为 `initex`，即 Proxifier 的厂商标识

这些不是真实的公网 IP：`127.x.x.x` 是回环地址，任何连接 `127.170.10.x` 的程序实际上是在连回本机，而不是访问互联网。

当时 Proxifier 配置文件（profile）中开启了：

```xml
<ViaProxy enabled="true" />
```

这表示 Proxifier 通过代理解析主机名，并给应用返回假的本地 IP。该机制只有在 Proxifier 后续拦截到连接、并把假 IP 映射回原域名时才能正常工作。但该 profile 同时存在大量 Direct 规则，例如：

```xml
<Applications>clash-win64.exe</Applications>
<Action type="Direct" />
```

于是 `Clash` 自身拿到 `api.github.com -> 127.170.10.16` 这样的假 DNS 结果，随后 Proxifier 又按 Direct 规则放任 `Clash` 直连这个假回环 IP——结果连接失败。

### 解决步骤

1. 打开 Proxifier
2. 进入 `Profile -> Name Resolution`
3. 禁用 `Resolve hostnames through proxy` / `DNS via proxy`
4. 保存 profile
5. 执行：

```cmd
ipconfig /flushdns
```

6. 重启 Proxifier、`Clash` 及受影响的程序

### 更合理的配置思路

对于本机环境，更干净的设计是：让 Windows 常规 DNS 负责域名解析，Proxifier 只负责把选定的应用程序通过 `Clash` 的本地 SOCKS 端口代理。不要在保留 Direct 规则的同时使用 Proxifier 全局 fake DNS。

如需微信相关进程直连（不走代理），可将下列进程加入 Direct 规则：

```text
wetype_server.exe; wetype_renderer.exe; wetype_update.exe; wxdrive_x64.exe
```

`Tailscale` 可能引起了部分混淆，但 `127.170.10.x` 与 `fd00:696e:6974:6578` 记录的来源明确指向 Proxifier 的 DNS 模式。
