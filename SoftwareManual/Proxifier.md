
# TroubleShotting


##### 发现有一部分程序无法连接网络，DNS解析失败

This is not Tailscale DNS anymore. The main problem is Proxifier fake DNS / remote DNS mode leaking into direct
  connections.

  Key evidence from your machine:

  - rawchat.cn resolves to 127.170.10.30
  - drive.weixin.qq.com resolves to 127.170.10.88
  - Windows DNS cache contains many 127.170.10.x records with huge TTLs
  - AAAA records are fd00:696e:6974:6578::...
  - 696e:6974:6578 decodes to initex, which is Proxifier’s vendor

  So these are not real public IPs. 127.x.x.x is loopback. Any program connecting to 127.170.10.x is connecting back to
  your own PC, not the internet.

  Your Proxifier profile has this enabled:

  <ViaProxy enabled="true" />

  That means Proxifier is resolving hostnames through proxy and giving apps fake local IPs. This only works when
  Proxifier later catches the connection and maps the fake IP back to the original hostname. But your profile also has
  many Direct rules, including:

  <Applications>clash-win64.exe</Applications>
  <Action type="Direct" />

  So Clash itself is getting fake DNS like api.github.com -> 127.170.10.16, then Proxifier lets Clash connect directly
  to that fake loopback IP. Result: failure.

  What to do

  1. Open Proxifier.
  2. Go to Profile -> Name Resolution.
  3. Disable Resolve hostnames through proxy / DNS via proxy.
  4. Save profile.
  5. Run:

  ipconfig /flushdns

  6. Restart Proxifier, Clash, and affected apps.

  For your setup, the cleaner design is: let normal Windows DNS resolve names, and let Proxifier only proxy selected
  applications through Clash’s local SOCKS port. Do not use Proxifier global fake DNS while also having direct rules.

  Also add these WeChat-related processes to your direct rule if you want them unproxied:

  wetype_server.exe; wetype_renderer.exe; wetype_update.exe; wxdrive_x64.exe

  Tailscale may have triggered part of the confusion, but the 127.170.10.x and fd00:696e:6974:6578 records point
  directly to Proxifier’s DNS mode.
