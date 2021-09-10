# brew 简介

### 概念

Homebrew, Mac 的包管理工具，类似 yum 和 apt-get


### 基础知识

Homebrew 的两个术语：

- Formulae：软件包，包括了这个软件的依赖、源码位置及编译方法等；
- Casks：已经编译好的应用包，如图形界面程序等

Homebrw相关的几个文件夹用途：

- bin：用于存放所安装程序的启动链接（相当于快捷方式）
- etc：brew安装程序的配置文件默认存放路径
- Library：Homebrew 系统自身文件夹
- Cellar：通过brew安装的程序将以 [程序名/版本号] 存放于本目录下

### brew 安装

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

### 常用命令

``` shell
# 查看brew版本
$ brew -v

# 查看帮助
$ brew --help
$ brew -h

# brew 更新
$ brew update

# 查看包的详细信息
$ brew info xxx

# 列出本地软件库
$ brew list

# 查看软件库版本
$ brew list --versions

# 搜索软件包（支持正则表达式）
$ brew search xxx

# 卸载软件包
$ brew uninstall xxx

# 安装包
$ brew install xxx
$ brew install [--cask] xxx
```

> cask 加与不加的区别：
>
> brew 是下载源码解压，然后 ./configure && make install ，同时会包含相关依存库，并自动配置好各种环境变量
>
> brew cask 是针对已经编译好了的应用包（.dmg/.pkg）下载解压，然后放在统一的目录中（Caskroom），省掉了自己下载、解压、安装等步骤

> - brew install 用来安装一些不带界面的命令行工具和第三方库
> - brew cask install 用来安装一些带界面的应用软件

### brew 安装常用软件

```bash
# vscode
brew install --cask visual-studio-code

# v2rayu
brew install --cask v2rayu

# upic
brew install --cask upic

# node
brew install node
```