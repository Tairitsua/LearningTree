# K8S集群部署要求

> 治理留痕（2026-09-30）：
> ① 文末新增"参考资料"节，由原 `Deployments/K8S部署笔记.md`（外链清单）并入，源文件已 `git rm`；
> ② 隐私脱敏：时钟服务器内网 IP 已替换为 `192.168.x.x`（原值见 `_governance/migration-log-cloudnative.md`）；
> ③ 笔误修正：`im` → `vim`；"openEuler 软件源"命令块中错乱的全角（2）（3）（3）（4）编号已整理为顺序命令；
> ④ `net.ipv4.tcp_tw_recycle` 处加注"[内核 4.12 起已移除，待事实核查确认]"；
> ⑤ "系统资源限制配置"一节 AI 粘贴痕迹重排为正式笔记。

## 节点要求

1. 同步时钟服务器时间
2. 永久关闭 `SELinux`
3. 永久关闭虚拟内存交换
4. 永久关闭防火墙
5. 创建 `/etc/resolv.conf` 文件，并配置 `DNS` 服务器 `IP` 地址。
6. 执行 `vi /etc/security/limits.conf` 修改系统最大句柄数限制，在文件中添加 `* soft nofile 65535` 和 `* hard nofile 65535`。再重启服务器。
![](../../attachments/Pasted%20image%2020230814163237.png)
7. 将五个服务器中 `/etc/yum.repos.d/openEuler.repo` 重命名备份，然后将配置文件 `openEuler.repo` 拷贝到5个服务器的 `/etc/yum.repos.d` 路径下。
这是配置 `yum` 仓库地址
注意这个目录下不要有多个 `.repo` 文件，它似乎只会识别一个去处理。
验证是否配置成功可以尝试 `yum list`

8. 在服务器分别执行 `dnf clean all`，`dnf makecache` 命令
`dnf clean all` 和 `dnf makecache` 命令是与 `DNF` 包管理器相关的命令，用于在基于 `RPM` 的 `Linux` 发行版上安装、更新和删除软件包。以下是它们的功能说明：

- `dnf clean all` 删除从仓库元数据生成的所有缓存文件。这有助于解决因损坏或过时的元数据引起的包安装问题。它还通过删除不必要的文件来释放一些磁盘空间
- `dnf makecache` 下载并缓存已启用仓库的元数据。这可以通过避免不必要的下载来加速包安装过程。它还确保元数据是最新的，并与远程仓库保持一致

9. 执行 `yum install -y conntrack socat tar`

`Conntrack` 是一个 `Linux` 内核模块，可以跟踪网络连接。它允许内核跟踪所有当前活动的网络连接，并提供通过用户空间接口操作它们的方法。
`Socat` 是一个命令行工具，可以建立两个双向字节流并在它们之间传输数据。它可以用于各种目的，如调试、测试和网络探索。它经常用作 `Linux` 系统中 `netcat` 工具的替代品。

10. 重启集群每个节点的服务器。


## 防火墙配置

> `openEuler`

- 运行 `systemctl stop firewalld.service` 命令来停止防火墙服务。
- 运行 `systemctl disable firewalld.service` 命令来禁用防火墙服务的自动启动。
- 运行 `systemctl status firewalld.service` 命令来查看防火墙服务的状态，确认已经关闭。

## 时钟配置

多服务器之间通信要保持时钟一致，特别是内网无法连接外部时间时。

### 服务端配置

1. `vi /etc/chrony.conf`

2. 在配置文件里添加以下配置

   ```ini
   server xxx.xx.xx.xx(服务端 IP) iburst (本机配置,自己既是服务端又是客户端)
   allow
   ```

![](../../attachments/Pasted%20image%2020230814155326.png)

3. 按顺序执行以下语句

修改时区与同步设置：

```bash
timedatectl set-timezone 'Asia/Shanghai'
timedatectl set-ntp 1
```

重启服务：

```bash
systemctl enable chronyd
systemctl restart chronyd
```

查看状态：

```bash
systemctl status chronyd
```

![](../../attachments/Pasted%20image%2020230814155551.png)

### 客户端配置

> **客户端同步时钟前必须关闭防火墙及 `SELinux`**

1. `vi /etc/chrony.conf` 修改 `server`

   ```ini
   server 192.168.x.x iburst （IP 为时钟服务器 ip）
   ```

![](../../attachments/Pasted%20image%2020240616173908.png)

2. 启用和重启服务：

   ```bash
   systemctl enable chronyd
   systemctl restart chronyd
   ```

3. 查看状态：

   ```bash
   systemctl status chronyd
   ```

4. 最后输入 `timedatectl` 命令，看到如下图所示则时钟同步成功。

![](../../attachments/Pasted%20image%2020230814155516.png)



## DNS服务器配置

配置好后可以使用 `dig www.xxx.com` 命令，随便输入一个网站，它会读取 `/etc/resolv.conf` 下 `nameserver` 的配置然后尝试发送请求解析，如果有回应，说明 `DNS` 配置正确。
`resolv.conf` 文件内容如下：

```bash
nameserver 188.xxx.xxx.xxx
```

可以运行 `systemctl restart NetworkManager` 命令重启使其强制生效。
## 系统资源限制配置

`Linux` 中定义的系统句柄最大数量的默认值取决于句柄的类型。句柄有多种类型，如文件描述符、进程、套接字、内存映射等，每种都有不同的限制和不同的更改方法：

- **每进程文件描述符数**：通过 `ulimit -n` 检查，默认值通常是 1024，可通过编辑 `/etc/security/limits.conf` 更改。
- **系统级文件描述符数**：通过 `cat /proc/sys/fs/file-max` 检查，默认值取决于可用内存的数量，可通过 `sysctl fs.file-max=number` 更改。
- **每用户最大进程数**：通过 `ulimit -u` 检查，默认值通常是 4096，可通过编辑 `/etc/security/limits.conf` 更改。
- **系统级最大进程数**：通过 `cat /proc/sys/kernel/pid_max` 检查，默认值通常是 32768，可通过 `sysctl kernel.pid_max=number` 更改。
- **系统 `TCP/IP` 连接（本地端口范围）**：通过 `cat /proc/sys/net/ipv4/ip_local_port_range` 检查，默认值通常是 32768 到 61000，可通过 `sysctl net.ipv4.ip_local_port_range="min max"` 更改。其他影响 `TCP/IP` 连接的参数还有 `net.ipv4.tcp_fin_timeout`、`net.ipv4.tcp_tw_recycle` 和 `net.ipv4.tcp_tw_reuse`。
- **每进程内存映射最大数量**：通过 `cat /proc/sys/vm/max_map_count` 检查，默认值通常是 65530，可通过 `sysctl vm.max_map_count=number` 更改。

> `net.ipv4.tcp_tw_recycle` 参数[内核 4.12 起已移除，待事实核查确认]，新内核上已无法通过 `sysctl` 调整该参数。

以上只是 `Linux` 中系统句柄及其限制的一些例子，可能还有其他类型的句柄具有不同的限制和更改方法，可查阅 `Linux` 文档了解更多。

## openEuler 软件源

可参考 [搭建 repo 服务器 (openeuler.org)](https://docs.openeuler.org/zh/docs/22.03_LTS/docs/Administration/%E6%90%AD%E5%BB%BArepo%E6%9C%8D%E5%8A%A1%E5%99%A8.html)

1. 将 `openEuler-22.03-LTS-everything-x86_64-dvd.iso` 镜像拷贝到服务器的 `root` 目录下。

2. 按顺序执行以下命令：

   ```bash
   mkdir -p /mnt/iso
   mount openEuler-22.03-LTS-everything-x86_64-dvd.iso /mnt/iso/
   mkdir /opt/openeuler_repo/
   cp -r /mnt/iso/* /opt/openeuler_repo/
   vim /etc/yum.repos.d/openEuler.repo
   ```

3. 在 `openEuler.repo` 文件里写入以下内容：


   ```ini
   [base]
   name=base
   baseurl=file:///opt/openeuler_repo
   enabled=1
   gpgcheck=1
   gpgkey=file:///opt/openeuler_repo/RPM-GPG-KEY-openEuler
   ```


4. 执行 `yum -y install nginx` 安装 `nginx`，将 `/etc/nginx/nginx.conf` 文件重命名备份，然后将 `nginx.conf` 拷贝到 `/etc/nginx` 路径下。

`nginx.conf` 文件内容修改如下：

```nginx
user  nginx;
worker_processes  auto;                          # 建议设置为core-1
error_log  /var/log/nginx/error.log  warn;       # log存放位置
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;                 # 服务器名（url）
        client_max_body_size 4G;
        root         /usr/share/nginx/repo;                 # 服务默认目录

        location / {
            autoindex            on;            # 开启访问目录下层文件，这里一定要记得开，不然会有403Forbidden问题
            autoindex_exact_size on;
            autoindex_localtime  on;
        }

    }
}
```

可以用软链接方式将 `repo` 文件夹链接到 `nginx` 目录下：

```bash
ln -s /opt/openeuler_repo /usr/share/nginx/repo
```

5. 依次执行以下命令启动 `nginx`：

   ```bash
   systemctl enable nginx
   systemctl start nginx
   systemctl status nginx
   ```

6. 打开浏览器访问本机 `IP` 地址，出现下图则部署成功。

## 参考资料

1. [B站视频教程](https://www.bilibili.com/video/BV15g411F7pj/?spm_id_from=333.337.search-card.all.click&vd_source=c5c41a7b3fb9dadc2ff98bb690cf1433)

2. [KubeSphere 离线安装文档](https://www.kubesphere.io/zh/docs/v3.3/installing-on-linux/introduction/air-gapped-installation/)

3. [在 VMware vSphere 上安装 KubeSphere](https://www.kubesphere.io/zh/docs/v3.3/installing-on-linux/on-premises/install-kubesphere-on-vmware-vsphere/#%E9%83%A8%E7%BD%B2-keepalived-%E5%92%8C-haproxy)

> 2、3 为 KubeSphere v3.3 时点文档，新版本文档结构可能有变化。

存储方案：`Ceph` 使用 `ceph-deploy` 部署。
