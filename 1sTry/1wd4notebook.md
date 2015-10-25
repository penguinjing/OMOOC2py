# 1wd4 线下公开课 笔记
### 公开课对自己触动最大的 top 3 内容  

##### 1. 调试代码 (Debug) 其实有方法  

自己v2版的极简日记程序调试，前后花了接近6小时。当时的做法运行发现出错后，根据系统给出的提示错误，  
代码一遍遍在自己脑海里跑思考哪里出错。现在回想这种调试方法不科学但当时并没意识到。 

往后我应该参考大妈演示中的"解决学院经典问题，强调官方文档"视频中的调试方法模型进行代码调试。

* 明确位置
* 选定怀疑
* 查询文档
    * [本地文档 - Python 2.7.10 documentation](https://docs.python.org/2/download.html)  
    * 基本语法  
    * 内建函数 => dir() / help()  

先将与出问题无关代码/功能逐步隔离屏蔽掉，缩小出问题时触发的行为/代码范围(# 单行注释或''' 整段注释 ''' )。这相当于犯罪现场的净化，有问题的让他继续运行，没有问题的部分关闭。  

不确定哪里出问题，考虑插入print 语句，让Python打印出来对象/变量值或对象/变量类型(print type() )进行检查，以查找错误核心。  

查询文档时也值得参考官方教程和库说明


##### 2. 每次采用代码范式模板作为基础开始编程

以前完全没想到过这种方法，可以增加效率的同时避免遗漏。有好的方式以后的编程都采用这种方式。  
下面是大妈的模板(Coding paradigm)，供参考：
```
# -*- coding: utf-8 -*-
#! /usr/bin/env python
# heading statement
'''
文件说明
作者信息
版本自述
...
'''
# 全局引用
import sys
# 全局变量
PATH = "/path/2/work dir"
# 函式撰写区
def foo():
    pass
    return None

# 自检区
if __name__ == '__main__':
    if 1 != len(sys.argv):
        print '''Usage:
$ python main..py
        '''
    else:
        foo()

```

##### 3. Keep Calm and Use the Force  

我的理解是保持冷静，使用自己内生的直觉（力量）来思考如何拆解编程任务实现程序代码。这其中我认为最重要的第一步是理清程序目的(Purpose)和目标(Target)，可能的话与客户沟通确认目的与目标理解是否正确。然后根据目的和目标所涉及各功能项目拆解及各部分代码实现。

往后我写程序代码前，先把思考后的程序实现目的与目标，拆分后的各功能名称及实现思路写进开发文档中才正式编写代码实现。在测试过程中不断回顾程序要达到的目的与目标，看各功能部分组合起来后是否真正达成程序目标与目的。  

别忘了：用最小代价解决问题！

### 当天公开课其他部分笔记

* 上周(0W)作业表扬  

    * wp-Lai  
    * aJiea  
    * Zoe   

* REPL 交互命令环境  
含义：Read-Eval-print loop(读入，运行，输出，循环)  
[REPL wiki介绍链接](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)  
  在REPL中可以获得的帮助：  
    * help() - 用来查看某一Python关键字或函数如何使用  
    * dir() - 用来报告当前环境中有哪些对象, 各对象可进行什么操作,   各操作有什么内置hook  

* 大妈使用的各种工具参考  
[PyENV](https://github.com/yyuu/pyenv)  
[pyenv - virtualenv](https://github.com/yyuu/pyenv-virtualenv)  
== > [  ] 学习如何使用配置PyENV  
[mdp - a command-line based markdown presentation tool](https://github.com/visit1985/mdp)  
[sphinx](http://sphinxsearch.com/)  
[Python 2.7.10 documentation for downloads](https://docs.python.org/2/download.html)  
[lynx - text-based web browser](http://lynx.invisible-island.net/)  
[CLI 终端中的终端录屏 - tmux](https://en.wikipedia.org/wiki/Tmux)  

* UTF-8 字符集  
所有文档/程序代码存成UTF-8格式  
    * Shell首选代码是UTF-8  
    * 代码保存成UTF-8  
    * 输出也是UTF-8  

* The Zen of Python, by Tim Peters  
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!  
  
* Pythonista 八荣八耻  
以动手实践为荣 , 以只看不练为耻;  
以打印日志为荣 , 以单步跟踪为耻;  
以空格缩进为荣 , 以制表缩进为耻;  
以单元测试为荣 , 以人工测试为耻;  
以模块复用为荣 , 以复制粘贴为耻;  
以多态应用为荣 , 以分支判断为耻;  
以Pythonic为荣 , 以冗余拖沓为耻;  
以总结分享为荣 , 以gui求其解为耻;  

* 所有东西都能教授，但！**求知欲**和 **学习能力** 除外  
~shell909090 151019 00:11