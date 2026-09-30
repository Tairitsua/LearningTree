# CMD

> 治理留痕（2026-09-30）：本文件由原 `SoftwareManual/CMD.md` 的 `# CMD` 章拆分而来（其中 `## PowerShell` 整章并入 [Powershell](Powershell.md)，`# 注册表`、`# 批处理基础` 分别拆为 [注册表](注册表.md)、[批处理](批处理.md)）。原稿见 [_archive/SoftwareManual/CMD-原稿](../_archive/SoftwareManual/CMD-原稿.md)。
> 本次格式修复：`### 端口占用问题` 中 ①②③ 标号改为 Markdown 序号；`doskey` 引用的 XP 版 technet 文档标注"[历史文档]"；`### 调整网络优先级` 中一处不成对的反引号已修正。

## Windows

### 反复异常蓝屏

可能是更新驱动导致系统文件损坏，可通过命令尝试修复

```powershell
sfc /scannow
# sfc是检查所有系统文件并将组件存储（Component Store，存放在WinSxS文件夹下）里的已签名文件替换掉被破坏的系统文件。
```

或使用

```powershell
Dism /Online /Cleanup-Image /ScanHealth
Dism /Online /Cleanup-Image /CheckHealth
Dism /Online /Cleanup-Image /RestoreHealth
```

### 解除文件关联

```cmd
assoc.mp4 # 获取mp4关联的文件类型
# .mp4=WMP11.AssocFile.MP4
ftype | findstr "MP4" # 查找文件类型关联的打开程序
# PotPlayerMini64.MP4="D:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe" "%1"
# 通过下面两条置空
assoc.mp4=
ftype PotPlayerMini64.MP4=
```

### 入域

计算机名联系部门相关人员，应是一人一计算机名。
确认入域时，会提醒输入域账号密码验证，这时候如果这个计算机名没有关联到域账号，那会显示找不到路径之类的错误提示，这时候要联系域管理员关联上，才能使用域账号密码登陆。

![](../attachments/Pasted%20image%2020230726170452.png)

### 虚拟机桥接联网

有线一根，连接后虚拟机上连接该有线网卡，然后在虚拟机适配器中开启连接共享（虚拟机设置NAT模式即可），如果之前已经开了共享，那需要**重新开启共享**，不然有线网卡无法加入。
如果偶尔会掉线，则需要通过ping 命令一直ping对端PC。刷新arp路由表。


### 游戏强制全屏的窗口化

`Alt+Enter`

#### 分屏窗口移动
使用键盘快捷键（通用但可能因软件限制而效果不同）
Alt + Space（打开窗口菜单）然后 M（移动）
首先按下Alt + Space组合键，这会打开当前活动窗口的系统菜单。这个菜单包含了诸如还原、最小化、最大化等操作选项。
接着按下M键，此时鼠标指针会变成一个四向箭头，表示进入了窗口移动模式。
然后你可以使用方向键（上、下、左、右）来移动窗口。按一下方向键，窗口就会朝相应的方向移动一个像素单位。如果一直按住方向键，窗口会持续移动。
当你把窗口移动到可以看到的屏幕区域后，再使用鼠标来精确调整窗口位置。

Windows 键 + 左 / 右方向键
如果你的双屏是水平排列的，使用Windows + 左方向键可以将窗口移动到左边的屏幕（如果窗口在右边屏幕），Windows + 右方向键可以将窗口移动到右边的屏幕（如果窗口在左边屏幕）。不过这种方法在另一个屏幕无法正常显示的情况下可能无法准确操作，因为系统可能会根据屏幕状态做出不同反应。但在一些情况下，它可以帮助你快速切换窗口所在的屏幕位置，你可以多尝试几次看看是否能将窗口移动到可见的屏幕区域。

#### 应用自启动最小化

`start /min D:\Euynac\Dictionary\GoldenDict\GoldenDict.exe`

保存为`.bat`

cmd运行`shell:startup`打开自定义自启动列表放入该bat文件

`start "" /B /D "D:\Desktop\bongo_cat_mver_0.1.6_64" "Bongo Cat Mver.exe"`

`start`的参数可以看帮助文件学习, 主要的坑就是第一个参数. 空引号是用来指定新窗口的标题。在 `start` 命令里，第一个引号内的内容会被当作新窗口的标题。若省略这部分，后续带引号的程序路径会被错误识别为窗口标题。所以使用空引号能避免这种情况，让命令正确识别后续的程序路径。

#### win11启动组策略gpedit.msc

```bat
@echo off

pushd "%~dp0"

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"

pause
```

#### 解决UTF8编码问题

`CHCP 65001`

解决python乱码问题：python等项目多采用使用`setenv.bat`文件去临时创建一个运行环境，在其中添加：

```sh
export PYTHONUTF8=1  # linux / macOS
set PYTHONUTF8=1  # windows
```

千万注意`bat`文件中使用`set xxxx=xxxx`时，结尾不要含有空格，否则也会当作传入的值。

#### 关闭/启用默认使用管理员权限打开程序

程序所在的exe右键属性中，可以控制是否默认以管理员权限打开。

#### 修复系统损坏文件

管理员模式运行

`sfc /scannow`

#### 换回win10右键

切换到旧版右键菜单：

```bat
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

恢复回Win11右键菜单：

```bat
reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f
```

重启Windows资源管理器生效：

`taskkill /f /im explorer.exe & start explorer.exe`

#### 自启动程序

文件位置打开后，按 Windows 徽标键 + R，键入`shell:startup`，然后选择"确定"。这将打开"启动"文件夹。

将该应用的快捷方式从文件位置复制并粘贴到"启动"文件夹中。

#### WIFI密码

`netsh wlan show profiles` 查看所有连接过的WiFi配置

`netsh wlan show profiles "TP-LINK_5G_4926" key=clear`  查看配置文件

#### 查看文件md5等值

Certutil.exe作为证书服务的一部分安装。您可以使用Certutil.exe转储和显示证书颁发机构（CA）配置信息，配置证书服务，备份和还原CA组件，以及验证证书，密钥对和证书链。

```text
1.  certutil -hashfile filename MD5
2.  certutil -hashfile filename SHA1
3.  certutil -hashfile filename SHA256
```

#### 快速切换到指定文件夹

文件资源管理器直接打开那个文件夹然后在url地址栏填上cmd打开

#### 强行删除权限不足的文件（需要管理员权限）

```bat
set path="XX"

takeown /F %path% /r /d y

cacls %path% /t /e /g Administrators:F

rd /s /q $path$
```

#### 打开cmd当前目录

```text
1.  explorer .
2.  explorer %cd%
3.  start .
4.  start %cd%
```

#### Windows键失效

尝试`FN+Windows`键一起连续按多几次（十几次），解锁win键

#### 不重启使环境变量修改生效

以修改环境变量"PATH"为例，修改完成后，进入DOS命令提示符，输入：`set PATH=C:` ，关闭DOS窗口。再次打开DOS窗口，输入：`echo %PATH%` ，可以发现PATH 值已经生效。

DOS窗口必须重启后环境变量才有效。

#### 以树形形式展示目录结构

`tree`

#### 判断程序是否以管理员运行

任务管理器中，详细信息栏，选择列，选择开启"特权"一栏。

#### Windows服务启动类型无法修改，为灰色

可以尝试使用命令修改：`sc config "Muse Hub Background Service(服务属性中的服务名称)" start=demand`
如果报错拒绝访问，可能是因为权限不足。即使是管理员权限，也无法修改。其实还有一个电脑的最高特殊权限，所以还可以通过这个软件：`M2-Team NSudo Launcher`[GitHub - M2TeamArchived/NSudo: [Deprecated, work in progress alternative: https://github.com/M2Team/NanaRun] Series of System Administration Tools](https://github.com/M2TeamArchived/NSudo) （不过需要下载Preview版本，8.2版本会token生成错误）来启动 `services.msc`来修改。

如果还是为灰色，那就说明这是个流氓软件，只能通过注册表修改了：
参考路径：`计算机\HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\<服务名称>`
里面注册表项`Start`即为启动类型：`1 - 自动延时启动 2 - 自动 3 - 手动 4 - 禁用`。修改后重启电脑即可。
还有个方案是可以将注册表中的`Security`（有这个说明控制了权限）随便改个名字，让它无效，这样就可以手动控制启动类型了。注册表详情见 [注册表](注册表.md)。

### 端口占用问题

Hyper-V 会保留部分tcp端口，开始到结束范围内的端口不可用, 使用如下命令查看保留的端口：

`netsh interface ipv4 show excludedportrange protocol=tcp`

保留的端口是随机的，每次重启电脑都会改变，因此可以通过重启电脑来解决。

除了重启电脑，也可以运行`net stop winnat`停止 winnat 服务，然后再运行`net start winnat`启动 winnat 服务。

让Hyper-V再随机初始化一些端口保留，如果正好没随机到要用的端口，那一次成功。如果还是随机到了要用的端口，那就只能多来几次。

也可以永久排除保留端口：

1. 在运行 Docker 之前，以管理员身份运行 powershell

2. 使用以下命令永久排除6379作为保留端口(如果端口被占用需要重启一次电脑)

`netsh int ipv4 add excludedportrange protocol=tcp startport=6379 numberofports=1 store=persistent`

提示：关键在于`store=persistent`参数表示持久化信息

**上面的命令可以通过修改numberofports参数保留startport开始的多个端口**

3. 再次运行 `netsh interface ipv4 show excludedportrange protocol=tcp` 命令可以看到6379端口已被排除(带有*号标记)

还有一种办法是重新设置一下「TCP 动态端口范围」，让Hyper-V只在我们设定的范围内保留端口即可。可以以管理员权限运行下面的命令，将「TCP 动态端口范围」重新设定为`49152-65535`。如果你觉得这个范围太大，还可以改小一点。

```bat
netsh int ipv4 set dynamic tcp start=49152 num=16384
netsh int ipv6 set dynamic tcp start=49152 num=16384
```

然后重启电脑即可。

重启电脑后，再运行命令`netsh int ipv4 show dynamicport tcp`查看动态端口范围，发现确实已经修改为了`49152-65535`。

### 网络问题

#### 对于受限网络WIFI会自动断开

To disable the Windows Network Connectivity Status Indicator (NCSI) active test, use the Group Policy Editor (`gpedit.msc`) to enable the "Turn off Windows Network Connectivity Status Indicator active tests" setting.  Navigate to `Computer Configuration` > `Administrative Templates` > `System` > `Internet Communication Management` > `Internet Communication settings` and change the policy to Enabled.  After making the change, restart your computer or run `gpupdate /force` to apply it.

#### 使用代理

- **Windows Settings Proxy**: The proxy you configure in _Settings → Network & Internet → Proxy_ applies to apps using the WinINET API (like Edge, Internet Explorer, or apps that rely on system networking).
- **CMD & Console Tools**: Many command-line tools (like `curl`, `git`, `npm`) rely on **WinHTTP** or their own proxy settings, not WinINET. That’s why CMD doesn’t automatically use the proxy you set in Windows Settings.
- Some tools respect environment variables: (like `curl`)
```bat
set http_proxy=http://proxyserver:port
set https_proxy=http://proxyserver:port
```



## 设置Alias

[Doskey [历史文档] | Microsoft Learn](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490894(v=technet.10)?redirectedfrom=MSDN)（XP 时代 technet 版文档，仅作参考）

`doskey npd=notepad $2 $1`

即`npd aaa bbb = notepad bbb aaa`

`doskey prt=echo $*`

即 `prt xxx xxx xx = echo xxx xxx xx`

`doskey newline=echo $1 $T echo $2`

其中`$t`或`$T`是新的一行，即多执行下一行。

`doskey /macros` 显示设置的宏定义

`doskey macroname=` 删除宏定义（将已设置的宏设置为null）

但是注意，它是临时的，需要做如下操作变成永久：

[command line - Create permanent DOSKEY in Windows cmd - Super User](https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd)

## 文件操作

注意批处理`*.bat` 读取文件是用`ANSI`编码的，所以如果是用的`UTF-8`编码之类的，读取中文之类会乱码。因此需要先转`ANSI`编码，具体可以使用文本编辑器里的编码选项中进行转换文件的编码。

`cd`命令只能在当前盘符使用。切换硬盘直接输入`d:`、`e:`等。

## 网络

| 命令                                  | 参数                                                                                                                                       | 简介                                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| netstat                             | -a 显示一个所有的有效连接信息列表，包括已建立的连接（ESTABLISHED），也包括监听连接请求（LISTENING）的那些连接。 -b 显示在创建每个连接或侦听端口时涉及的可执行程序。 -n 以数字形式显示地址和端口号。 -o 显示拥有的与每个连接关联的进程 ID。 | net status 显示网络连接、路由表和网络接口信息，可以让用户得知有哪些网络连接正在运作。 不带参数则是显示活动的TCP连接 netstat -aon\|findstr "80"（以80端口为例） 其他用例： 查看某个端口具体被那个应用占用 tasklist \| findstr "PID" |
| set http_proxy set https_proxy      | =socks5://127.0.0.1:1080 或http也可以                                                                                                        | CMD设置临时代理（永久需要在环境变量中设置）可以用curl测试，不能使用ping。                                                                                                            |
| netsh interface ipv4 show neighbors |                                                                                                                                          | 查看局域网邻居ip                                                                                                                                             |
| tracert                             |                                                                                                                                          | 路由跟踪，指示到目标地址经过的路由IP                                                                                                                                   |
|                                     |                                                                                                                                          |                                                                                                                                                       |
|                                     |                                                                                                                                          |                                                                                                                                                       |

### 调整网络优先级

通过 PowerShell 命令调整网络适配器优先级

1. 查看网络适配器信息
  `Get-NetIPInterface | Where-Object { $_.InterfaceAlias -match 'Wi-Fi|以太网' } | Select-Object InterfaceAlias, InterfaceIndex, AddressFamily, InterfaceMetric`


2. 调整接口优先级
    - 找到无线网络和有线网络的接口索引（InterfaceIndex）
    - 降低无线网络的接口跃点数（值越小优先级越高）

  设置无线网络优先级（假设接口索引为12）
  `Set-NetIPInterface -InterfaceIndex 12 -InterfaceMetric 10`

  设置有线网络优先级（假设接口索引为15，值要大于无线网络）
  `Set-NetIPInterface -InterfaceIndex 15 -InterfaceMetric 20`
