# -*- coding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明 
- 在上周开发基础上，完成极简交互式笔记的桌面版本
- 需求如下：
    - 每次运行时合理打印出过往的所有笔记
    - 一次接受输入一行笔记
    - 保存为本地文件

作者信息 penguinjing
版本自述 V1.0
'''
from os.path import exists 
import Tkinter as tk  # import Tkinter module
import sys

reload(sys)
sys.setdefaultencoding('utf-8')  # supporting Chinese display in label widget(or maybe in whole frame)

def get_all_records(f):
    content = 'All previous records: \n'
    for current_line in f:
        content = content + current_line[:-1] + '\n'
    return content

def save(*args): 
    line = content_input.get()
    current_file.write(line + '\n')

log_name = 'mydiary.log'

if exists(log_name) == True:
    current_file = open(log_name, 'r+')
    text_rec = get_all_records(current_file)
    #lines_inputs(current_file)

else:
    current_file = open(log_name, 'w')
    text_rec = 'There are no previous dairy records\n'
    #lines_inputs(current_file)
 
App = tk.Tk()
App.title('Mini Diary Writer')

content_input = tk.StringVar()  #initil the variable for Entry wideget input

theLabel = tk.Label(App, text=text_rec)
theLabel.pack(side='top', fill='both', expand=True)
TextEntry = tk.Entry(App, text='New diary goes', textvariable=content_input)
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)

TextEntry.pack()
ButtonWrite = tk.Button(App, text='Save into diary', command=save) #[TODO:Edward.hu]
ButtonQuit = tk.Button(App, text='Quit', command=quit)
ButtonWrite.pack()
ButtonQuit.pack()
App.mainloop()
current_file.close()
print 'current file was closed'
