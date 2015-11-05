### 1wd4~2wd3 GUI极简日记程序 任务描述

本周整体任务概述：

- 在上周开发基础上，完成极简交互式笔记的桌面版本
- 需求如下：
    - 每次运行时合理打印出过往的所有笔记
    - 一次接受输入一行笔记
    - 保存为本地文件
- 时限：1wd4 ~ 2wd3
- 发布：发布到各自仓库的 '_src/om2py2w/2eex0' 目录中
- 指标：
    - 包含软件使用说明书：'README.md'
    - 能令其他学员根据说明书，运行系统。完成所有功能

Ref：
[24.1. Tkinter  -- Python interface to Tcl/Tk](https://docs.python.org/2.7/library/tkinter.html)  
[Tkinter reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter)  
[An Introduction To Tkinter](http://effbot.org/tkinterbook/tkinter-index.htm)
[IDLE and tkinter with Tcl/TK on Mac OS X | Python.org](https://www.python.org/download/mac/tcltk/)  

[24.2 ttk -- Tk themed widgets](https://docs.python.org/2.7/library/ttk.html)
[24.4 ScrolledText -- Scrolled Text Widget](https://docs.python.org/2.7/library/scrolledtext.html)  

- Tk operate in "loop" That is transparent to the developer.
- Widgets are assigned parents, which contain other widgets, etc.
- Layout managers handle widget placement
- Widgets can have events "bound" to them and respond accordingly.

- Tkinter provides three geometry manager
    - absolute (avoid this)
    - pack (layout)
        - Extremely simple
        - specify a side
        - Parent sizes itself to minimally fit everything
        - Not particularly flexible for complex layouts
    - grid (layout)
        - Closer to other toolkits
        - Frames are laid out in a grid
        - resizing can be handled via expand arguments
- Widgets
    - tkinter historically provides common, simple widgets
    - Considered a shortcoming
         - Missing more advanced widgets
    - Button / Frame / Label / Label with / Image / Listbox / Menu / Scale / Scrollbar / Spinbox / Text
- ttk Widgets
    - "Overrides" drawing of tkinter widgets
        - Drawing now handled by theme engine
    - Introduces new, modern widgets
    - Change the "styles"
        - ttk.Style().theme_names()
        - ttk.Style().theme_use(style)
- ttk Notebook
    - Provides modern paged notebook of frames, accesible via tabs
    - Sensible functionality

- ttk Treeview
    - Implements tree, list, columned list, etc.
- ttk et cetera
    - Combobox
    - CheckButton
    - RadioButton
    - Progressbar
    - Separator
    - Sizegrip

- Canvas
    - Allows fro simple primitive drawing within a Tk widget
    - Opens up the door for custom widget behavior


GUI 101 安装    
~ 极简交互式日记的桌面版本    
需要安装嘛?  
=> 不需要安装，采用python内置库Tkinter。需要时导入库，import   

如何确认可生成标准桌面窗口?  
=> 运行程序，出现标准窗口即可（最好带工具栏）    

GUI 101 排版    
~ 极简交互式日记的桌面版本    
Tk 能使用什么控件?  
=> Label, Entry, Button, Text,   

我们的软件,需要哪几种?!  
=> 我们需要Entry, Button, Text  

怎么控制默认窗口的:  尺寸   
=> 自动适应  

控件位置  
=> .pack() 方法  

中文能显示嘛?    


GUI 101 后台     
~ 极简交互式日记的桌面版本    
上周的 CLI 工具如何结合 Tk ?  
能直接调用嘛?  
=> 采用按button按钮控件，激发一个event, 由后台( .mainloop() )去捕捉，相应执行第一周已实现的代码块。    

读取日记文件的print  
=>替换为text 控件显示过往日记内容   

 提示用户输入文字的Raw_input  
=>替换为entry控件及相应按钮        

GUI 101 友好      
~ 极简交互式日记的桌面版本    
桌面软件的友好包含什么要素?  
=> 包含窗口标题，包含最小化，最大化和关闭按钮。  

在我们的软件中如何体现?  
如何用最小成本体现?    
