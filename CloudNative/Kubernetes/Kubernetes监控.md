# Kubernetes监控

> 治理留痕（2026-09-30）：原文件另含 `## Git`、`## 发布`、`## 网络` 三个离题章节，已分别迁至 `SoftwareManual/Git.md`（"Git 提交规范"）、`CloudNative/CICD/发布策略.md`、`Kubernetes/网络.md`（"排查DNS问题"节）；原文件首行空行已修复。

## 监控对象

### 数据中心
- **风火水电、温度、湿度**（动环监控）

### 网络监控
- 全国网络链路情况
- 延迟、丢包（`DNS`监控）

### 物理设备
- `CPU`温度
- 风扇转速
- 硬盘故障（带外监控）

### 操作系统
- `CPU`
- 内存
- `IO`（网络`IO`、磁盘`IO`）

- `Linux` 主机流量监控：`iftop` 可以实时监控当前主机和其他主机的通信流量命令
- `iotop` 主机`IO`监控
- `strace` 查看系统调用
- `lsof` 查看所有打开的文件

### 应用服务
- 应用组件：`Nginx`、`Tomcat`、`MySQL`、`Oracle`等

### 业务监控
- 每分钟订单量
- 日活
- 日新增用户数

> 业务应用要用`HTTP`暴露`health`接口，不要直接用端口是否存活

### 流量监控
- 基于`Web`访问的`PV`、`UV`
- 访问人群地域

### APM（应用性能管理）
- 端到端调用链
- 应用拓扑

### 日志监控
- 错误日志
- 访问日志
- 运行日志
- 设备日志

### 安全监控
- 系统审计
- 漏洞扫描
- `Webshell`扫描

### 舆情监控
- 微信、微博等新闻媒体


## 监控工具

### Elastic Stack（ELK Stack）

- **组成**：`Elastic Stack`主要包括以下组件：
    
    - **Elasticsearch**：一个分布式搜索和分析引擎。
    - **Logstash**：数据处理管道，支持收集、解析、变换数据。
    - **Kibana**：数据可视化工具，用户可以通过它创建图表和仪表板。
    - **Beats**：轻量级数据发送器，用于将数据从不同来源发送到`Logstash`或`Elasticsearch`。
- **用途**：
    
    - 集中式日志管理
    - 搜索和分析应用日志
    - 创建可视化仪表板和报告

### Prometheus

- **组成**：`Prometheus`主要包括以下组件：
    
    - **Prometheus Server**：核心组件，负责数据采集和存储。
    - **Alertmanager**：用于处理告警。
    - **Pushgateway**：支持短期任务推送指标。
    - **Exporter**：将监控数据从各种系统和服务导出给`Prometheus`。
    - **PromQL**：查询语言，用于查询监控数据。
- **用途**：
    
    - 指标监控和告警
    - 系统性能分析
    - 服务健康监测

### 关系与结合使用

- **互补性**：`Elastic Stack`主要用于日志数据的收集、存储和可视化，而`Prometheus`则专注于时间序列数据的指标监控和告警。
     
- **结合使用**：
    
    - **日志与指标关联**：可以通过将`Prometheus`的指标数据与`Elastic Stack`的日志数据关联，提供全面的系统监控视图。例如，当某个指标出现异常时，可以快速查看相关日志进行故障排查。
    - **数据可视化**：虽然`Prometheus`有自己的可视化工具（如`Grafana`），但也可以将`Prometheus`的指标数据导入`Elastic Stack`，利用`Kibana`进行更高级的可视化和分析。
    - **中央化存储**：将`Prometheus`的指标数据通过工具（如`Elasticsearch Exporter`）导入到`Elasticsearch`中，实现统一的数据存储和管理。
