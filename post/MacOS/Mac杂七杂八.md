# Mac使用总结

## 主机名、用户名

主机名、hostname 是一个东西，指的是你本地网络上的电脑可以通过主机名访问你的电脑。这个与 Linux 系统是一致的。

ComputerName，这个是 macOS 才有的东西。跟 Windows 上一样，表示的是电脑名称，给人看的。

对于 macOS 来说，它会按以下的顺序来确定主机名，直到获取到为止：

- 从以下文件中读取：`/etc/hostconfig`
- 从以下系统配置项读取：`/Library/Preferences/SystemConfiguration/preferences.plist` 中的 `System ▸ System ▸ HostName`
- 由本机 IP 地址的反向 DNS 查询获取
- 从以下系统配置项读取：`/Library/Preferences/SystemConfiguration/preferences.plist` 中的 `System ▸ Network ▸ HostNames ▸ LocalHostName`
- 如果以上方法都没获取到，就为默认的 `localhost`

终端中显示的用户名、主机名和提示符等等格式，都是通过环境变量文件（bashrc、bash_profile）中的环境变量`PS1` 来决定的。

终端左侧显示用户名和主机名，可以通过下面的方式修改：

```bash
# 查看 hostname
$ hostname
# or
$ scutil --get LocalHostName

# 修改 hostname
$ sudo scutil --set LocalHostName XXX

# 查看 ComputerName
$ scutil --get ComputerName

# 修改 ComputerName
$ sudo scutil --set ComputerName XXX
```

### scutil 工具

`scutil` 是个可动态访问 macOS 系统信息的交互式工具。

```bash
# 查看 DNS 配置
$ scutil --dns

DNS configuration

resolver #1
  nameserver[0] : 61.139.2.69
  nameserver[1] : 218.6.200.139
  if_index : 5 (en0)
  flags    : Request A records
  reach    : 0x00000002 (Reachable)
...

# 查看代理配置
$ scutil --proxy
<dictionary> {
  HTTPEnable : 0
  HTTPSEnable : 0
  ProxyAutoConfigEnable : 0
  SOCKSEnable : 0
}

# 查看网络配置
$ scutil --nwi
Network information

IPv4 network interface information
     en0 : flags      : 0x5 (IPv4,DNS)
           address    : 192.168.0.105
           reach      : 0x00000002 (Reachable)

   REACH : flags 0x00000002 (Reachable)
...
```

### DS_Store 文件

有时候修改目录下的文件后，会出现 `.DS_Store` 这样的一个文件。

`DS_Store` 文件（英文全称 Desktop Services Store），是一种由苹果公司的Mac OS X操作系统所创造的隐藏文件，目的在于存储目录的自定义属性，例如文件的图标位置或者是背景色的选择。相当于 Windows 下的 `desktop.ini`。

```bash
# git 目录下的操作 DS_Store文件
# 删除项目中的所有.DS_Store。这会跳过不在项目中的 .DS_Store
$ find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
# 将 .DS_Store 加入到 .gitignore
$ echo .DS_Store >> ~/.gitignore
```

如果你只需要删除磁盘上的 `.DS_Store`，可以使用下面的命令来删除当前目录及其子目录下的所有`.DS_Store` 文件:

```bash
$ find . -name '*.DS_Store' -type f -delete
```

也可以彻底禁止

```bash
# 禁止.DS_store生成
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE

# 恢复.DS_store生成
defaults delete com.apple.desktopservices DSDontWriteNetworkStores
```







