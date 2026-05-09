# Microsoft


## Microsoft Store

商店无法连接问题解决方案：

用clsah挂代理的话，开UWP应用网络回环，选中Microsoft Store等UWP应用再连接就正常了

Internet Options中 Advanced里面勾选 TLS1.0 到 TLS1.3，Connections中LAN Setting里面将 Proxy server里面Use a proxy server for your LAN (These settings will not apply to dial-up or VPN connections).去掉。 并勾上Automatically detect settings