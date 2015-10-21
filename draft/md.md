# Markdown 写作语言 私人介绍

## 背景

Markdown是种纯文本的标记语言，其语法目标"方便地在网上写作"，在打字的同时把排版也一起解决了，不用像Word里再去调格式。Markdown兼容HTML标签，任何文本编辑器都可以直接读取.md or .markdown文件 (Markdown文件)。很多Markdown的文字编辑器可以直接将Markdown文件输出PDF或HTML文件，便于网上发布。  

Markdown vs. Markdown GFM  

Github Favored Markdown(缩写GFM)是Github社会化编程网站采用的一种Mardkown写作语言的扩展，加强了便于在Github网站上沟通交流的特性。  

## 安装

Markdown语言本身并不需特别编辑器，但为了更方便的预览Markdown呈现效果，有些专用或特别对Markdown优化支持的编辑器可选择安装。

* [Mardkown Pad](http://markdownpad.com) - Windows
* [MacDown](http://macdown.uranusjr.com/) - Mac OS X
* [Sublime Text](http://www.sublimetext.com) - Win/Mac/Linux

其他适用于Markdown编辑器请见参考中《10分钟学会Markdown》一文。

## 配置

[Sublime Text](http://www.sublimetext.com) 是个优秀的跨平台代码/文本编辑器，为更好的编写/显示预览Markdown文字，需要相应配置才可实现。另外写文专述如何配置。

## 使用

1. 分级标签  
\# 便签内容 \# (一级标签)
\## 便签内容 \## (二级标签)
......
一直支持到六级标签(尾端的#不写也是可以的)  

2. 强调 / 斜体  
\** 加粗**
\*斜体*

3. 列表  
  \* / + / - 表示无序列表。数字1. 2. 3. 表示有序列表。

4. 分割线  
\***
\***  

5. 行内代码块引用  
\`引用内容`  

6. 代码块整段引用  
\```
\```  

7. 网站链接  
\[链接文字](链接本身)  

8. 图片链接  
\![链接文字](图片链接本身)  

9. 邮箱  
\<邮箱名@邮箱服务器名>  

10. 换行  
两个空格 + 回车

## 体验

--- 分级标题 ---

# 一级标题  
## 二级标题  
### 三级标题  
#### 四级标题  
##### 五级标题  
###### 六级标题  

--- <强调 / 斜体> ---

**加粗字体**  
*斜体*

--- <列表> ---  
    * 无序列表行1  
    * 无序列表行2  
        - 缩进列表行  
```  
    1. 有序列表行1
    2. 有序列表行2
    3. 有序列表行3  
```

--- <分割线> ---  
***  
这里是分割线
***  

--- 行内代码块引用 ---  

`引用内容`  

--- 代码块整段引用 ---  
```
这里是引用的代码块
```  

--- 网站链接 ---  
[Git官方网站](http://git-scm.com)  

--- 图片链接 ---  
![What a fucking day.jpg](http://upload-images.jianshu.io/upload_images/103327-9bacefc0e831fd2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240/format/jpg)  

--- 邮箱 ---  
<abc@abc.com>

--- 换行 ---

示意段落1  

示意段落2  


## 参考

视频：  
  - [GeeK系列 - 12分钟光速上手MarkDown](http://www.bilibili.com/video/av2793636/)  
   
文档：  
  - [10分钟学会Markdown](http://www.jianshu.com/p/15ab5501f1dc?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weibo)  
  - [Git Markdown文档](https://guides.github.com/features/mastering-markdown/)  
  - [GFM官方文档](https://help.github.com/articles/github-flavored-markdown/)  
  - [GUODongXiaRend的Github Flavored Markdown语法介绍](https://github.com/guodongxiaren/README)

