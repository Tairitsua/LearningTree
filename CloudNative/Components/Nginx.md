# Nginx


## 常见问题

### 配置location后不生效，仍路由到前端页面

可能是没有清理缓存，前端页面直接解决了路由请求。需要在 `F12` 中 `Application-Storage` 清理当前页面缓存

### 相关条目

- [`Kubernetes/故障排查`](../Kubernetes/故障排查.md)：`Nginx` 消息截断、获取用户真实 `IP` 两条排查记录。