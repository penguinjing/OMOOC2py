# 0W 本周整体任务概述：

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

任务模块思路拆解：  
  * 一次接收输入一行日记  
    => [ ] 1. 弹出对话框接收用户输入一行文本信息，存入一string变量info中  
  * 保存为本地文件  
    => [ ] 2. 把变量info的内容存入本地文件Dairy.txt中  
  * 再次运行系统时，能打印出过往的所有日记  
    => [ ] 3. 运行程序时，检测是否存有笔记记录文件:Dairy.txt文件。  
          a. 有的话，打印笔记文件内容，然后继续执行上面1).  部分接收用户输入的一行笔记内容。  
          b. 没有的话，直接执行1).部分。