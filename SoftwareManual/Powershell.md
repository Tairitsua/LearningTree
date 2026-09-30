# PowerShell

> 治理留痕（2026-09-30）：原 `SoftwareManual/CMD.md` 的 `## PowerShell` 整章已并入本文件（原 `###` 子节提升为 `##`，合并去重后无重复内容）。原稿见 [_archive/SoftwareManual/CMD-原稿](../_archive/SoftwareManual/CMD-原稿.md)。
> 事实修正：`获取电池寿命报告` 的 `powercfg` 命令原稿写作 `powercfg batteryreport output "D:\\battery_report.html"`（缺少 `/` 参数写法），已按正确语法修正为 `powercfg /batteryreport /output "D:\battery_report.html"`。

## 从单行base64执行

`powershell -EncodedCommand`

注意不是文本转base64，似乎是从字节流转的：

```powershell
$script = Get-Content "bongo-cat_runner.ps1" -Raw
$bytes = [System.Text.Encoding]::Unicode.GetBytes($script)
$encoded = [Convert]::ToBase64String($bytes)
$encoded | Set-Content "encoded.txt"
```

### 通过`VBS`运行脚本

```vbs
Set shell = CreateObject("Shell.Application")
Set fso = CreateObject("Scripting.FileSystemObject")

' PowerShell
psBase64 = "IwAgAEUAbgBhAGIAbABlACAAZABlAHQAYQBpAGwAZQBkACAA"

' Decode and save to a temporary ps1 file.
tempFolder = fso.GetSpecialFolder(2) ' 2 = TemporaryFolder
ps1Path = tempFolder & "\bongo_temp.ps1"

Set psFile = fso.CreateTextFile(ps1Path, True)
psFile.WriteLine "powershell -EncodedCommand " & psBase64
psFile.Close

' Run PowerShell script with administrator privileges.
shell.ShellExecute "powershell.exe", "-NoProfile -ExecutionPolicy Bypass -File """ & ps1Path & """", "", "runas", 1
```

## 安装SSH Server以支持SSH连接

```powershell
# 使用PowerShell以管理员权限执行，查看安装状态
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
# 安装Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# 初始化ssh服务器
net start sshd
# 或
Start-Service sshd

# 设为开机自启
Set-Service -Name sshd -StartupType 'Automatic'
# This is a PowerShell command that retrieves all firewall rules that have "ssh" in their name.
Get-NetFirewallRule -Name *ssh*

# 卸载
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# 添加防火墙规则
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH SSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22 -Program "C:\Windows\System32\OpenSSH\sshd.exe"

# ssh客户端生成ssh公钥与私钥，以使用无密码连接，将生成的公钥放到ssh服务端
ssh-keygen -q -b 2048 -P "" -f <hostname>_rsa -t rsa
# 具体操作： https://stackoverflow.com/a/69970152
```

仍然无效的可以使用如下方法安装
[Manually install OpenSSH in Windows Server](https://www.saotn.org/manually-install-openssh-in-windows-server/)

## 获取CPU温度

```powershell
$data = Get-WMIObject -Query "SELECT * FROM Win32_PerfFormattedData_Counters_ThermalZoneInformation" -Namespace "root/CIMV2"

@($data)[0].HighPrecisionTemperature
```

## 临时无限制模式

`pwsh -ExecutePolicy Unrestricted`

在当前会话有效

## 获取电池寿命报告

`powercfg /batteryreport /output "D:\battery_report.html"`

## 计算文件sha256

`Get-FileHash filePath`

`CertUtil -hashfile {PATH AND FILE NAME} {SHA256|MD5}`

## 同时使用WIFI与有线网络

首先使用`route print`查看路由表。
路由表有顺序优先级，越上面的优先级越高。
`0.0.0.0`指代所有目标？
![](../attachments/Pasted%20image%2020240616173732.png)
其中`192`部分为`WIFI`网关，`188`为有线网关（内网）。此时所有流量先走有线网，导致上不了外网。
而这种原因可能是配置了`DHCP`导致的，因此如果进行手动配置，填写好掩码、网关，则可以将优先级下降。
另外还有一种方式可以增加：
`route add 188.22.76.0 mask 255.255.255.0 188.22.77.1 -p`

> 将访问 188.22.76.0-188.22.76.255 网段的所有数据，通过 188.22.77.1 这个网关进行转发，其中`-p`是永久生效，默认是拔网线重启后就失效。

## 网络共享

开启网络适配器共享可以将两台机网络（通过有线网络连接）联通，连接后有两个网络适配器，开启共享，用于被共享的有线网络不要填默认网关。
共享成功后需要使用一个长时间的ping命令去ping主机（这样能保持两个主机稳定连通）
如果中途发现共享失效，这时候要重新去适配器上开启 `允许其他网络用户通过此计算机的Internet连接来连接`。并重新禁用启用用于共享的适配器


## 端口转发

`netsh interface portproxy add v4tov4 listenaddress=10.0.10.21 listenport=8081 connectaddress=192.168.33.111 connectport=8081`

`netsh interface portproxy` 表示端口映射列表

`add v4tov4` 表示添加的是`IPV4`到`IPV4`的端口

`listenaddress` 表示侦听的ip地址，填的是映射方

`listenport` 侦听的端口，可以与被映射的端口设置成不一样

`connectaddress` 被映射方（连接方）的ip地址

`connectport` 被映射方的端口

`netsh interface portproxy delete v4tov4 listenaddress=10.0.10.21 listenport=8081`

`netsh interface portproxy show all` 查看存在的转发

注意，浏览器出现`ERR_UNSAFE_PORT`错误不是因为服务器那边，而是浏览器本身定义了内置端口，这些端口是无法被使用的：

```text
1, // tcpmux
7, // echo
9, // discard
11, // systat
13, // daytime
15, // netstat
17, // qotd
19, // chargen
20, // ftp data
21, // ftp access
22, // ssh
23, // telnet
25, // smtp
37, // time
42, // name
43, // nicname
53, // domain
77, // priv-rjs
79, // finger
87, // ttylink
95, // supdup
101, // hostriame
102, // iso-tsap
103, // gppitnp
104, // acr-nema
109, // pop2
110, // pop3
111, // sunrpc
113, // auth
115, // sftp
117, // uucp-path
119, // nntp
123, // NTP
135, // loc-srv /epmap
139, // netbios
143, // imap2
179, // BGP
389, // ldap
465, // smtp+ssl
512, // print / exec
513, // login
514, // shell
515, // printer
526, // tempo
530, // courier
531, // chat
532, // netnews
540, // uucp
556, // remotefs
563, // nntp+ssl
587, // stmp?
601, // ??
636, // ldap+ssl
993, // ldap+ssl
995, // pop3+ssl
2049, // nfs
3659, // apple-sasl / PasswordServer
4045, // lockd
6000, // X11
6665, // Alternate IRC
6666, // Alternate IRC
6667, // Standard IRC
6668, // Alternate IRC
6669, // Alternate IRC
```
