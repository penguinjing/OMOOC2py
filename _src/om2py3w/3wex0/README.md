## LAN版 - 极简笔记程序

### 下载与安装

默认系统需有Python 2.7.11解释器，如没有请下载 [Python 2.7.11](https://www.python.org/downloads/release/python-2711/) 选择适合你系统的32位/64位版本安装。  
安装本程序，请先到该[地址](https://github.com/penguinjing/OMOOC2py/tree/master/_src/om2py3w/3wex0)，另存下载该程序(main.py)，然后在CMD命令行运行：  


### 运行程序

1. 先启动极简笔记程序服务器端
```
> Python main.py s
```

2. 然后运行客户端
```
> Python main.py c
```
客户端运行后输入服务器端地址（比如：192.168.1.2），即可看到`>>>`提示符，输入笔记内容，回车后当行文字传递去服务器端储存起来。

输入?/h/H 可获得帮助
输入r/sync 可同步服务器获得最新笔记内容
输入shutdown 可使得笔记服务器关闭
输入q/quit/bye 可推出客户端

### 待解决的Bug功能
待测试