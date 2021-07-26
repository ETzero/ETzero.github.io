# 安装brew

### 快捷安装

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

本质上就是去brew的官方github上下载脚本进行安装。其官方地址为：
```
https://www.github.com/homebrew/brew/
```

安装过程中可能会以下问题

#### 1. 连接被拒绝

命令开始执行时报出以下问题
```
curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused
```

#### 解决方案

##### 1、修改DNS

修改本地hosts的配置，将githubusercontent.com对于的ip直接写入的hosts文件中。

```
199.232.96.133 raw.githubusercontent.com
199.232.96.133 user-images.githubusercontent.com
199.232.96.133 avatars2.githubusercontent.com
199.232.96.133 avarars1.githubusercontent.com
```

推荐使用 `switchhosts`管理本地hosts

##### 2、直接下载brew的安装脚本到本地，然后执行

下载地址：
```
https://brew.sh
```


#### 2. 报告异常

安装快结束时，会报以下异常信息：
```bash
Error: Fetching /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core failed!
Error: Another active Homebrew vendor-install-ruby process is already in progress.
Please wait for it to finish or terminate it to continue.
Error: Failed to install Homebrew Portable Ruby (and your system version is too old)!
Failed during: /usr/local/bin/brew update --force --quiet
```

#### 解决方案

删除缓存的包，然后重新执行命令
```bash
cd cd /Users/yourname/Library/Caches/Homebrew/
rm -rf portable-ruby-2.6.3_2.yosemite.bottle.tar.gz

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```
