# 草案/原型
~ 此目录收集, 还在探索/思考 中的文文案

成熟后应该单立文档目录 长期增补

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
目的：用程序方式记录下日记。
目标：简单完成个交互式日记记录系统

模块思路拆解：
  * 一次接收输入一行日记
  => [ ] 1. 弹出对话框接收用户输入一行文本信息，存入一s变量info中
  * 保存为本地文件
  => [ ] 2. 把变量info的内容存入本地文件Dairy.txt中
  * 再次运行系统时，能打印出过往的所有日记
  => [ ] 3. 运行程序时，检测是否存有笔记记录文件:Dairy.txt文件。
          a. 有的话，打印笔记文件内容，然后继续执行上面1).部分接收用户输入的一行笔记内容。
          b. 没有的话，直接执行1).部分。

**[WIP]**要点具体实现思考：
  - 接收输入一行日记 -> infor = raw_input("Please type your dariy")
  - 保存本地文件 -> file.write()
    [ ] 查找相应文档，如何使用file.write() function
  - 打印出过往的所有日记 -> file.read() & print()


## 交互 101 - 脚本调用
首先，得有一个稳定的代码记录容器: 脚本
  * 以之前上传的`_src/om2py0w/0wex1/main.py`为例
  * 如何调用之?
  * 并确保每次调用返回相同的结果?

Ref:
[BeginnersGuideChinese - Python Wiki](https://wiki.python.org/moin/BeginnersGuideChinese)
[6. Modules - Python 2.7.10 documentation](https://docs.python.org/2/tutorial/modules.html)
[Code Style - The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)

## 交互 101 - 调用参数
然后, 脚本能接收外部数据的输入
  * 还是以`_src/om2py0w/0wex1/main.py`来操作吧
  * 如何做到调用main.py获得外部的数据的同时，不需要每次都修改代码?

Ref: 
[10. Brief Tour of the Standard Library - Python 2.7.10 documentation](https://docs.python.org/2/tutorial/stdlib.html#command-line-arguments)

## 交互 101 - 输入中文
接着最常用的要求, 脚本如何获得外部中文文本?

* 还是以`_src/om2py0w/0wex1/main.py`为例吧
* 如果给的参数是中文字符, 运行脚本会发生什么事儿? 
    * 解决之!

Ref:
[2. Using the Python Interpreter - Python 2.7.10 documention](https://docs.python.org/2/tutorial/interpreter.html#the-interpreter-and-its-environment)
[docopt - language for description of command-line interfaces](http://docopt.org/)

## 交互 101 - 持续交互
每次记录一行日志, 都要调用一次脚本嘛!? (嫌麻烦不?)
*  如何令`_src/om2py0w/0wex1/main.py` 可以一直运行, 等待我们的输入?
    * 或是接受其他命令?
    * 怎么退出脚本?

Ref:
[2. Built-in Functions - Python 2.7.10 documentation](https://docs.python.org/2/library/functions.html?highlight=raw_input#raw_input)

## 交互 101 - 输出为文件
每次记录的日志如何变成一个本地文件永久保存?
* 先不管数据结构, 就原样保存到文件(比如txt格式的)中吧！
  * 文本怎么实现换行?
  * 是否要加日期?
  * 中文要用什么编码?

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


## 进展
- 151018 Penguin写下思路
- 150316 大妈创建