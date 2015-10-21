## 0wd4~1wd3 本周整体任务概述：

* 完成一个极简交互式日记系统，需求如下：
    * 一次接收输入一行日记
    * 保存为本地文件
    * 再次运行系统时，能打印出过往的所有日记
* 时限: 0wd4 ~ 1wd3
* 发布: 发布到各自仓库的`_src/om2py0w/0wex1/`目录中
* 指标:  

    * 包含软件使用说明书: `README.md`
    * 能令其他学员根据说明书, 运行系统, 完成所有功能

***
目的：用程序方式记录下日记  
目标：简单完成个交互式日记记录系统

** 模块思路拆解：**  

* 一次接收输入一行日记  
> 弹出对话框接收用户输入一行文本信息，存入一string变量名line中

* 保存为本地文件  
> 把变量line的内容存入用户用命令行参数方式输入的本地文件(名)中

* 再次运行系统时，能打印出过往的所有日记  
> 运行程序时，检测是否存有笔记记录文件:Dairy.txt文件  
>   a. 有的话，打印笔记文件内容，然后继续执行上面1.部分接收用户输入的一行笔记内容  
>   b. 没有的话，直接执行1.部分  

要点具体实现思考：  

+ 接收输入一行日记 -> line = raw_input("Please type your dariy")  
+ 保存本地文件 -> file.write()  
  [X] 查找相应文档，如何使用file.write() function  

+ 打印出过往的所有日记 -> file.read() & print()  


## 交互 101 - 脚本调用
首先，得有一个稳定的代码记录容器: 脚本  

  * 以之前上传的`_src/om2py0w/0wex1/main.py`为例  
  * 如何调用之?  
  >进入文件存放目录，在命令行方式运行：`Python main.py` 的方式调用运行该程序。  
  * 并确保每次调用返回相同的结果?
  >采用同样的方式运行，就可返回同样的结果。"电脑是傻蛋！同样的运行条件，只能返回同样的结果。"

Ref:
[BeginnersGuideChinese - Python Wiki](https://wiki.python.org/moin/BeginnersGuideChinese)  
[6. Modules - Python 2.7.10 documentation](https://docs.python.org/2/tutorial/modules.html)  
[Code Style - The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)  

## 交互 101 - 调用参数  
然后, 脚本能接收外部数据的输入

* 还是以`_src/om2py0w/0wex1/main.py`来操作吧  
* 如何做到调用main.py获得外部的数据的同时，不需要每次都修改代码?  
> 采用命令行参数传递的方式，程序第一行：`import sys`，然后调用字符串变量`argv`，使用`argv[1:]`。  
> argv[0]是运行的Python程序名本身(*.py)  
> 第一参数是 argv[1]  
> 第二参数是 argv[2]  
> ...依此类推

Ref:   
[10. Brief Tour of the Standard Library - Python 2.7.10 documentation](https://docs.python.org/2/tutorial/stdlib.html#command-line-arguments)  

## 交互 101 - 输入中文
接着最常用的要求, 脚本如何获得外部中文文本?  

* 还是以`_src/om2py0w/0wex1/main.py`为例吧  
* 如果给的参数是中文字符, 运行脚本会发生什么事儿?   
> 中文字符处理采用程序内写上语言编码集申名 # -\*- coding: encoding -\*-  
> 通常在第一行申明 # -\*- coding: utf-8 -\*-
    * 解决之!  

Ref:  
[2. Using the Python Interpreter - Python 2.7.10 documention](https://docs.python.org/2/tutorial/interpreter.html#the-interpreter-and-its-environment)  
[docopt - language for description of command-line interfaces](http://docopt.org/)  

## 交互 101 - 持续交互  
每次记录一行日志, 都要调用一次脚本嘛!? (嫌麻烦不?)  

*  如何令`_src/om2py0w/0wex1/main.py` 可以一直运行, 等待我们的输入?  
> 采用`while true:`无限循环语句，实现程序运行后一直运行，不自动退出。  

* 或是接受其他命令?  
> 采用if 条件判断，判断输入的值=特定字符串，就执行相应命令
```
if line == 'finish':
  break
```
* 怎么退出脚本?  
> 提示客户输入特定字符，退出循环语句部分，最后调用文件关闭功能`file.close()` 安全退出。

Ref:  
[2. Built-in Functions - Python 2.7.10 documentation](https://docs.python.org/2/library/functions.html?highlight=raw_input#raw_input)  

## 交互 101 - 输出为文件  
每次记录的日志如何变成一个本地文件永久保存?  

* 先不管数据结构, 就原样保存到文件(比如txt格式的)中吧！
> 采用`file.write()`方法来写入文件  

    * 文本怎么实现换行?
    > 每行文本末尾加个Newline(换行字符) 代码写作`\n` ，可用来实现文本换行。
    * 是否要加日期?  
    > 暂时不加，后续翻阅稳定，查找date 函数/方法
    * 中文要用什么编码?  
    > 没看过其他人写中文程序用别的编码，就UTF-8吧。

Ref:  
[open() 2. Built-in Functions - Python 2.7.10 documentation](https://docs.python.org/2/library/functions.html?highlight=raw_input#open)  
[5.Built-in Types - Python 2.7.10 documentation](https://docs.python.org/2/library/stdtypes.html#file.write)  

## 交互 101 - 回读文本数据  
那么, 最后一个功能就能串联起来成为一个mini软件了！  
* 每次运行`_src/om2py0w/0wex1/main.py`时  
* 怎么自动将过往的日志都打印出来？  
* 细节:  
  * 如何找到日志文件?  
  * 如何打开日志文件?  
  * 如何读取文件内容?  
  * 如何输出日志?  
  * ...  
  * 中文输出OK嘛？  

Ref:  
[open() 2. Built-in Functions - Python 2.7.10 documentation](https://docs.python.org/2/library/functions.html?highlight=raw_input#open)  
[5.Built-in Types - Python 2.7.10 documentation](https://docs.python.org/2/library/stdtypes.html#file.readline)  

## 调错 - Debugging

#### v1  
argv[1] 参数变量外面加''，变为字符串(string), 并未正确传递日记文件变量名。  
`file.open('argv[1]', 'a')`  

更改为：  
`file.open(argv[1], 'a')`

#### v2  
文件写入方法(method)  
`fname.write('%s \n') line`

发现敲错，更改为的:  
`fname.write('%s \n') % line`

还是不行。看来file.write() 方法括号内不支持采用格式化字符方式，替换变量字符+'\n' (newline回车行)  ,   
尝试更改为：  
`fname.write(line + '\n') `

运行程序系统仍提示错误:  
```  
  File "main.py", line 8
    fname = open(argv[1], 'a')
                             ^
IndentationError: unindent does not match any outer indentation level
```  

看起来命令行提醒是对齐错误，检查前后的括号用法没有错误。  
无意中选中全部代码，发现:
```
  print argv[1]  => 这一行最前端是回车在Sublime Text中自动生成的Tab制表符，要死，如不是全部选中还看不出是空格。
    fname = open(argv[1], 'a')
    print fname.read()
```

替换全部Tab制表符为空格。全选所有代码，检查是否修改完成。

再运行程序，系统提示file.open() 打开模式不对。
```  
用Google搜索: python file.open mode
```
第一个链接：
[Python built-in open function: difference between modes](http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r)  
看过该链接信息后, 确定应该用 `file.open(r+)` 方式打开。

继续运行程序，系统在用户输入完一行文字按回车键后，继续报错（命真苦呀）:  
```  
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    fhand.write(line + '\n')
IOError: [Errno 0] Error
```

前后尝试修改半小时，没有头绪。只有放弃先去洗澡。中间想到既然上面file.open()模式的问题，那file.write() 也可以用同样关键字`python file.write mode`模式搜索得来. Google后看了前三个文档仍没头绪。

突然一下想到应把报错代码输入Google 当关键字再搜索下: `IOError: Errno 0`  
第二个结果吸引了我。[Python - IOError: [Errno 0] Error. What is Triggering this Error](http://stackoverflow.com/questions/19283118/python-ioerror-errno-0-error-what-is-triggering-this-error-in-my-code)

从这篇文档说明，我看到file.read()执行完后，文件指针指向末尾EOF。  
其建议在 `file.write()` 之前添加一句: `file.seek(0, 2) #`

不明觉厉，只能再搜索下[Python官方文档](/docs.python.org/2) 确认其用法，发现关于[file.seek的说明](https://docs.python.org/2/library/stdtypes.html?highlight=file.seek#file.seek) 

Bingo! 看来就是它了. 新增进代码中, 运行测试ok, 解决问题收工睡觉. 

回想下这8小时编程调试，还是花太多时间困在自己头脑中运行调试除错上。

* 应该牢记任务目标，以最小成本完成任务。
* 不断用Google 搜索错误代码/错误线索，搜索官方文档，可以更早解决问题。



## 进展
- 151021 Penguin 完成第一版
- 151018 Penguin 写下思路