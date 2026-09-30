# RabbitMQ

> 治理留痕（2026-09-30）：原 `Components/消息中间件.md` 全文并入本文件"概念"一节（同主题去重合并），源文件已 `git rm`；其 `•`/`◦` 列表符已转为标准 Markdown 列表，标题层级相应下调一级。

## 概念

在消息队列系统（如`RabbitMQ`）中，主题（`Topic`）、交换机（`Exchange`）和队列（`Queue`）是核心概念，共同协作实现消息的灵活路由和分发。以下是它们的定义、作用及关系：

### 队列（Queue）

- **是什么**：
  队列是消息的最终存储位置，用于缓存生产者发送的消息，等待消费者处理。
  - **类比**：相当于收件人的"邮箱"，消息被投递到邮箱后，收件人（消费者）按顺序取走。

- **核心特性**：
  - **持久性**：队列可以设置为持久化（消息在服务器重启后仍保留）。
  - **独占性**：队列可以声明为排他（仅允许一个消费者连接）。
  - **自动删除**：队列在无消费者时自动删除（需配置 `auto-delete`）。

- **用途**：
  消费者从队列中拉取（pull）或订阅（subscribe）消息进行处理。

### 交换机（Exchange）

- **是什么**：
  交换机是消息的路由中心，负责接收生产者发送的消息，并根据规则将消息分发到绑定的队列。
  - **类比**：相当于邮局的"分拣中心"，决定信件（消息）应投递到哪些邮箱（队列）。

- **核心特性**：
  交换机通过 **类型（Type）** 决定路由逻辑，常见的类型有：
  - **直连（Direct）**：消息的 `routing key` 必须与队列绑定的 `binding key` **完全匹配**。
  - **扇出（Fanout）**：广播模式，消息发送到所有绑定的队列（忽略 `routing key`）。
  - **主题（Topic）**：基于 `routing key` 的通配符（`*` 或 `#`）匹配队列。
  - **头（Headers）**：根据消息头（Headers）属性匹配队列（不常用）。

- **用途**：
  解耦生产者和消费者，生产者只需将消息发送到交换机，无需关心消息如何路由到队列。

### 主题（Topic）

- **是什么**：
  主题是交换机的一种类型（Topic Exchange），支持基于 `routing key` 的通配符匹配规则，允许消息灵活路由到多个队列。

- **核心规则**：
  - `routing key` 格式：以 `.` 分隔的字符串（如 `user.created`）。
  - **通配符**：
    - `*`：匹配一个单词（如 `user.*` 可匹配 `user.created`，但不能匹配 `user.created.email`）。
    - `#`：匹配零或多个单词（如 `user.#` 可匹配 `user.created` 和 `user.created.email`）。

- **示例场景**：
  - 生产者发送消息：`routing key = "order.payment.success"`。
  - 队列绑定到交换机时使用通配符：
    - 绑定键 `order.*` → 接收所有以 `order.` 开头的消息。
    - 绑定键 `#.success` → 接收所有以 `.success` 结尾的消息。

- **用途**：
  实现基于内容的多条件路由，例如日志分类、事件通知等场景。

### 三者的协作流程

1. **生产者**发送消息到 **交换机**，并指定 `routing key`。
2. **交换机**根据类型（如 Topic）和 `routing key` 匹配规则，将消息路由到符合条件的 **队列**。
3. **消费者**从 **队列** 中获取消息进行处理。

### 实际应用场景

#### 场景 1：订单系统（Topic Exchange）

- **交换机类型**：Topic。
- **队列绑定规则**：
  - `order.created` → 处理订单创建事件。
  - `order.#` → 订阅所有订单相关事件。
  - `payment.success` → 处理支付成功事件。
- **优势**：灵活的路由规则，避免为每个事件单独创建队列。

#### 场景 2：日志收集（Fanout Exchange）

- **交换机类型**：Fanout。
- **队列绑定**：所有日志处理服务绑定到该交换机。
- **优势**：日志消息广播到所有消费者，实现实时备份和分析。

### 关键配置（以 RabbitMQ 为例）

创建交换机（Topic 类型）：

```bash
rabbitmqadmin declare exchange name=my_topic_exchange type=topic
```

创建队列并绑定到交换机：

```bash
# 创建队列
rabbitmqadmin declare queue name=order_created_queue

# 绑定队列到交换机，设置 binding key
rabbitmqadmin declare binding source=my_topic_exchange destination=order_created_queue routing_key=order.created
```

### 总结

- **队列**：消息的存储单元，消费者直接操作的对象。
- **交换机**：消息的路由中心，决定消息流向哪些队列。
- **主题**：一种交换机类型，支持通配符匹配的路由规则。

通过合理配置三者，可以实现高效、灵活的消息分发机制。

## 常见命令

在 `RabbitMQ` 中，可以使用 `rabbitmqctl` 命令行工具快速清除所有队列和交换机。以下是具体操作步骤和注意事项：

### 1. 清除所有队列

命令：

```bash
# 列出所有队列并逐行删除（适用于所有队列无依赖的场景）
rabbitmqctl list_queues -q name | xargs -I {} rabbitmqctl delete_queue "{}"

# 或强制删除（即使队列正在使用）
rabbitmqctl list_queues -q name | xargs -I {} rabbitmqctl delete_queue "{}" --force
```

参数说明：

- `list_queues -q name`：静默模式（`-q`）列出所有队列的名称。
- `xargs -I {}`：将队列名逐个传递给 `delete_queue` 命令。
- `--force`：强制删除队列（即使有未消费的消息或活跃的消费者）。

### 2. 清除所有交换机

命令：

```bash
# 列出所有交换机并逐行删除（排除系统默认的 amq.* 交换机）
rabbitmqctl list_exchanges| grep -v "amq\." | awk '{print $1}' | xargs -n1 -I {} rabbitmqadmin delete exchange name={}
```

### 3. 注意事项

1. **数据丢失风险**：
   - 此操作会永久删除所有队列中的消息和交换机配置，**确保已备份必要数据**。
   - 生产环境慎用！建议仅在开发、测试环境或明确需要重置时执行。

2. **依赖关系检查**：
   - 如果队列绑定了交换机，删除交换机会导致绑定关系失效，但不会自动删除队列。
   - 若需彻底清理，建议先删除队列，再删除交换机。

3. **默认保留的交换机**：
   - 系统默认的 `amq.*` 交换机（如 `amq.direct`, `amq.topic`）不会被删除。它们是 RabbitMQ 内部创建的，删除后会在需要时自动重建。

### 4. 扩展：重置 RabbitMQ 节点

如果希望彻底重置整个 RabbitMQ 节点（删除所有数据，恢复到初始状态）：

```bash
# 停止 RabbitMQ 服务
rabbitmqctl stop_app

# 重置节点
rabbitmqctl reset

# 重新启动服务
rabbitmqctl start_app
```

- **此操作会删除所有队列、交换机、用户、权限、虚拟主机（vhost）等**，仅保留默认配置。

### 5. 验证清理结果

```bash
# 确认队列已清空
rabbitmqctl list_queues

# 确认交换机已清空（仅保留系统默认的 amq.*）
rabbitmqctl list_exchanges
```

## 问题

队列未删除无法修改诸如 `x-max-len` 的配置，建议在使用 `dapr` 进行本地 `RabbitMQ` 调试时将 `deletedWhenUnused` 设置为 `true`
