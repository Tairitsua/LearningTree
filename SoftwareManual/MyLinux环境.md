# MyLinux

> 治理留痕（2026-09-30）：本文件由原 `SoftwareManual/WSL.md` 的 `# MyLinux` 章拆分而来。原稿见 [_archive/SoftwareManual/WSL-原稿](../_archive/SoftwareManual/WSL-原稿.md)。
> 抽取留痕：原 `### ~/.zshrc` 下的 412 行 `.zshrc` 全文配置已抽取为独立配置文件 [zshrc.conf](../attachments/zshrc.conf)，此处保留说明与链接，内容一字未改。
> 本次格式修复：`## 配置bash为zsh` 下直接使用 `####` 的子标题提升为 `###` 以避免层级跳跃。

## 基于Docker

把docker镜像当作linux虚拟机来使用

```dockerfile
FROM centos:7
RUN yum install -y vim bash-com* openssh-clients openssh-server iproute cronie net-tools wget
RUN yum group install -y "Development Tools"
RUN yum clean all
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV LANG=zh_CN.UTF-8
docker build . -t mylinux
docker run -it -d -p 6666:22 --hostname mylinux1 --name mylinux1 --privileged=true mylinux /usr/sbin/init
# 以特权模式进入可以使用systemctl命令（特权模式必须运行/sbin/init，用于启动dbus-daemon）
docker exec -it mylinux1 /bin/bash # 进入容器
passwd root # 输入两次强制设置弱密码
```

## 安装常用包

### kali
```sh
apt install wget # 可从Web下载文件
apt install net-tools
apt install dirsearch # web目录扫描
apt install hydra # web密码爆破
apt install libgmp-dev libmpc-dev libmpfr-dev # gmpy2 dependencies
apt install dos2unix # 常见shell脚本回车问题
```


### python

```sh
pip install PyCryptodome gmpy2 pwntools
```


## 安装自编译软件


```sh
# Git拉取，并编译需要的软件，比如bkcrack (源码其实可以拉去/usr/local/src大概)
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=install
cmake --build build --config Release
cmake --build build --config Release --target install

# 在工作目录下install文件夹内有二进制可执行文件
# 一般来说自编译的软件放在/usr/local/bin 目录下
# 一定要使用绝对路径进行软链接，不然无法识别
ln -s /root/xxx/bkcrack/install/bkcrack /usr/local/bin

# 此时已经生效了，如果没生效检查一下环境变量作用范围是不是有那个/usr/local/bin
echo $PATH


```

> `bkcrack`、`cryptohack` 等自编译/容器化的 CTF 工具清单另见 [CTF/Toolbox/工具清单](../CTF/Toolbox/工具清单.md)。

## Linux命令手册
[jaywcjlove/linux-command: Linux命令大全搜索工具，内容包含Linux命令手册、详解、学习、搜集。https://git.io/linux (github.com)](https://github.com/jaywcjlove/linux-command)
轻松通过 `docker` 部署 `linux-command` 网站。

```shell
docker pull wcjiang/linux-command
```

```shell
docker run --name linux-command --rm -d -p 9665:3000 wcjiang/linux-command:latest
```


## 配置bash为zsh


```bash
chsh -s /bin/zsh
```

### ~/.zshrc

完整的 `.zshrc` 配置（Kali 默认 zsh 配置的基础上，追加了 Windows Docker 路径、代理/CTF 工具别名与若干 shell 函数）已抽取为独立配置文件：[zshrc.conf](../attachments/zshrc.conf)

> 注意，自己在使用反引号、`$()`等操作时，在sh脚本中的执行效果和预期的的问题，它先执行那一部分作为结果替换到脚本中，因此自己在配置 `.zshrc`等文件时，注意执行顺序。`$PWD`等环境变量也一样，脚本第一次运行时候已经决定了结果。除非使用转义符。

Best of all, use a function instead of an alias. A function lets you write the command exactly as you would normally without _any_ extra quotes or escaping.



## Docker 代理问题

docker 两种代理，一个是 docker desktop 及 cli 使用的，配置在 docker desktop `Network` 中设置，或通过 `Docker daemon` 配置文件设置。

```json
{
  "proxies": {
    "http-proxy": "http://proxy.example.com:3128",
    "https-proxy": "https://proxy.example.com:3129",
    "no-proxy": "*.test.example.com,.example.org,127.0.0.0/8"
  }
}
```



一个是 docker client 使用的（如构建镜像），` Builds and containers use the configuration specified in this file.` 需要在 `~/.docker/config.json` 中配置。
[Proxy configuration | Docker Docs](https://docs.docker.com/engine/cli/proxy/#configure-the-docker-client)

注意在 `Windows` 下，执行 `docker cli` 相关命令是在 `WSL`下的，所以需要修改成如下配置：

```json
"proxies": {
		"default": {
			"httpProxy": "http://host.docker.internal:41315",
			"httpsProxy": "http://host.docker.internal:41315",
			"noProxy": "localhost,127.0.0.1"
		}
	},
```

注意，在 `windows` 下的配置要生效，不仅要重启`docker desktop`还需要 `wsl --shutdown`。

> 最后发现不能用环境变量，似乎环境变量优先级最高，Clash的全局模式就是设置了环境变量

好像还是有问题，最终通过Docker Desktop自动使用系统代理解决
