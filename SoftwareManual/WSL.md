# WSL

> 治理留痕（2026-09-30）：本文件由原 `SoftwareManual/WSL.md` 的 `# WSL` 章拆分而来（`# Kali`、`# MyLinux` 章分别拆为 [Kali](Kali.md)、[MyLinux环境](MyLinux环境.md)）。原稿见 [_archive/SoftwareManual/WSL-原稿](../_archive/SoftwareManual/WSL-原稿.md)。
> 本次格式修复：裸外链 `<https://...>` 改为带标题链接；2 个无语言代码块补标 `text`/`ini`；`## WSL连接宿主机代理` 下直接使用 `####` 的子标题提升为 `###` 以避免层级跳跃。

可以通过windows terminal的配置，将启动目录改到与运行目录相同，方便直接使用linux相关工具

## 文件管理
可以直接在windows按下面的方式访问：
`\\wsl$`
`\\wsl.localhost\kali-linux\root`

## 命令

[WSL 的基本命令 | Microsoft Learn](https://docs.microsoft.com/zh-cn/windows/wsl/basic-commands)

|                                                                                                           |                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| wsl --list --online                                                                                       | 列出可用的linux发行版                                                                                                                                                              |
| wsl --install -d kali-linux                                                                               | 下载kali-linux并安装启动                                                                                                                                                          |
| wsl --shutdown                                                                                            | 终止所有子系统                                                                                                                                                                    |
| wsl --terminate docker-desktop-data                                                                       | 终止指定的子系统, 如 docker-desktop-data                                                                                                                                            |
| wsl --export docker-desktop-data F:/WSL/docker-desktop-data/docker-desktop.tar                            | 将子系统导出为tar包                                                                                                                                                                |
| wsl --unregister docker-desktop-data                                                                      | 使用wsl命令注销并删除子系统                                                                                                                                                            |
| wsl --import docker-desktop-data F:/WSL/docker-desktop-data F:/WSL/docker-desktop-data/docker-desktop.tar | 重新导入子系统到指定目录，然后tar包可以删除了                                                                                                                                                   |
| wsl -l -v                                                                                                 | 列出当前安装的wsl列表，以及版本信息                                                                                                                                                        |
| cat /etc/resolv.conf \| grep nameserver                                                                   | WSL 每次启动的时候都会有不同的 IP 地址，所以并不能直接用静态的方式来设置代理。WSL2 会把 IP 写在 /etc/resolv.conf 中                                                                                                |
| wsl -d(--distribution) \<Distribution Name\> --user \<User Name\>                                         | 若要通过特定用户运行特定 Linux 发行版，请将 \<Distribution Name\> 替换为你首选的 Linux 发行版的名称（例如 Debian），将 \<User Name\> 替换为现有用户的名称（例如 root）。 如果 WSL 发行版中不存在该用户，您将会收到一个错误。 若要输出当前用户名，请使用 whoami 命令。 |
| wsl --set-default \<Distribution Name\>                                                                   | 设定默认打开的Linux发行版                                                                                                                                                            |
| wsl --import kali-linux C:\WSL\kali-linux-new "C:\WSL\kali-linux\ext4.vhdx" --vhd --version 2             | 从vhd导入旧的子系统（建议用tar包导入）                                                                                                                                                     |

## WSL连接宿主机代理

[zinglix.xyz - WSL2 使用宿主机代理](https://zinglix.xyz/2020/04/18/wsl2-proxy/)


### 新版配置
新版本WSL遇到问题的：wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理
`wsl: A localhost proxy configuration was detected but not mirrored into WSL. WSL in NAT mode does not support localhost proxies.`

[Accessing network applications with WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/networking#auto-proxy)

[WSL issue #10753 的解决方案评论](https://github.com/microsoft/WSL/issues/10753#issuecomment-2041372912)


在Windows用户根目录`%USERPROFILE%`新建`.wslconfig`文件
```config
[wsl2]
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true


[experimental]
# requires dnsTunneling but are also OPTIONAL
bestEffortDnsParsing=true
# useWindowsDnsCache=true
autoMemoryReclaim=gradual  # gradual  | dropcache | disabled

```
然后`wsl --shutdown`关闭后重启wsl

### 脚本


```shell
#!/bin/sh
hostip=$(cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }')
wslip=$(hostname -I | awk '{print $1}')
port=<PORT> # 需要自行更改为proxy端口

PROXY_HTTP="http://${hostip}:${port}"
set_proxy(){
    export http_proxy="${PROXY_HTTP}"
    export HTTP_PROXY="${PROXY_HTTP}"
    export https_proxy="${PROXY_HTTP}"
	export HTTPS_PROXY="${PROXY_HTTP}"
git config --global http.proxy "${PROXY_HTTP}"
git config --global https.proxy "${PROXY_HTTP}"
}
# python如果无效的话，就在python执行的命令后加 --proxy=http://xxxxx吧
unset_proxy(){
    unset http_proxy
    unset HTTP_PROXY
    unset https_proxy
    unset HTTPS_PROXY
git config --global --unset http.proxy
git config --global --unset https.proxy
}



test_setting(){
    echo "Host ip:" ${hostip}
    echo "WSL ip:" ${wslip}
    echo "Current proxy:" $https_proxy
}

if [ "$1" = "set" ]
then
    set_proxy
elif [ "$1" = "unset" ]
then
    unset_proxy
elif [ "$1" = "test" ]
then
    test_setting
else
    echo "Unsupported arguments."
fi

alias proxy="source /xxx/proxy.sh"
```

另外可以在 `~/.bashrc` 中选择性的加上下面两句话，记得将里面的路径修改成你放这个脚本的路径。

```shell
alias proxy="source /xxx/proxy.sh" # 可以为这个脚本设置别名 proxy，这样在任何路径下都可以通过 proxy 命令使用这个脚本了，之后在任何路径下，都可以随时都可以通过输入 proxy unset 来暂时取消代理。

/xxx/proxy.sh set # 在每次 shell 启动的时候运行该脚本实现自动设置代理，这样以后不用额外操作就默认设置好代理啦~
```

注意，这代理不适用于某些不关注系统环境变量的程序，比如apt，firefox等。

默认情况下，WSL2是无法ping通HOST的，但能ping通宿主机，需要设置相应的防火墙规则使其支持ping通HOST。

如若遇到vEthernet 无法连接互联网的情况，可以通过联通主机的代理进行外网访问。

解决方案是直接重启电脑。猜测是hype-v的端口随机占用有概率导致无法连接问题

## 问题
### WSL 任何命令没有反应
一般是升级安装损坏的问题，需要手动通过安装包安装：[Releases · microsoft/WSL](https://github.com/microsoft/WSL/releases/)
安装过程中出现：`Could not write value  to key \SOFTWARE\Classes\Directory\shell\WSL.   Verify that you have sufficient access to that key, or contact your support personnel.` 诸如此类的问题，需要注册表编辑器修改相应文件夹System以及Adminstrator的权限为完全控制。

### WSL内部错误导致无网络异常

```text
wsl: 出现了内部错误。
Error code: CreateInstance/CreateVm/ConfigureNetworking/0x8007054f
wsl: Failed to configure network (networkingMode Mirrored), falling back to networkingMode None.
wsl: A localhost proxy configuration was detected but not mirrored into WSL. WSL in NAT mode does not support localhost proxies.
```

将`.wslconfig`配置修改为：
```ini
[wsl2]
networkingMode=mirrored
autoProxy=true
```

并将系统代理关闭

还有个方法是禁用所有网络适配器，关闭代理软件，然后重新开起来所有网络适配器，先别打开代理，看看恢复没，恢复后即可继续使用。

有次直接关闭代理的LAN、IPV6，然后好了，再打开这两个


### zsh语法高亮非常慢

输入第一块命令的时候，WSL2的zsh语法高亮特别慢，通过排查 `~/.zshrc`可以发现是`zsh-syntax-highlighting.zsh`的问题，遂上Github发现问题：
[syntax highlighting is super slow in WSL2 · Issue #790 · zsh-users/zsh-syntax-highlighting (github.com)](https://github.com/zsh-users/zsh-syntax-highlighting/issues/790)

其中有一个临时解决方案，禁用掉某个wsl2的功能（似乎是可以将windows的环境变量运用到wsl中，这也导致docker之类的用不了了）。

I solved this by excluding windows directories from `$PATH` by adding following in `/etc/wsl.conf`. Create the file if it doesn't exist

```ini
[interop]
appendWindowsPath = false
```

Then restart wsl with

```sh
wsl --shutdown
```
#### 添加需要的windows程序到环境变量

注意大小写
```zshrc
path+=( 
/mnt/c/Users/lesmo/AppData/Local/Microsoft/WindowsApps /mnt/c/Users/lesmo/AppData/Local/Programs/Microsoft VS Code/bin /mnt/c/Program Files/Docker/Docker/resources/bin /mnt/c/ProgramData/DockerDesktop/version-bin /mnt/c/WINDOWS 
)
```
