# -*- coding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明 
- 一次接收输入一行日记
- 保存为本地文件
- 再次运行系统时，能打印出过往的所有日记

作者信息 penguinjing
版本自述 V3.0
'''
'''
from os.path import exists

def print_all_records(f):
    line_count = 1
    print 'Previous dairy records: \n'
    for current_line in f:
        print '%i - %s' % (line_count, current_line[:-1])
        line_count +=1
    print '=' * 20

def lines_inputs(f):
    print 'Diary now... \n'
    while True:
        line = raw_input('Current >>> ')
        if line.strip() == '':
            continue
        if line == '?' or line == 'h' or line == 'H':
            print '^-^ \n \t input ?/h/H for help \n \t input q/bye quit the Dairy progame'
            continue
        if line == 'q' or line == 'bye':
            break
        f.write(line + '\n')

def main():
    log_name = 'mydairy.log'

    if exists(log_name) == True:
        current_file = open(log_name, 'r+')
        print_all_records(current_file)
        lines_inputs(current_file)

    else:
        current_file = open(log_name, 'w')
        print 'There are no previous dairy records:\n', '=' * 20
        lines_inputs(current_file)

if __name__ == '__main__':
    main()
'''

# Hello world by https://docs.python.org/2.7/library/tkinter.html
'''
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
'''
'''
# Hello world by liaoxuefeng
from Tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
#设置窗口标题:
app.master.title('Mini Dairy')
#主消息循环:
app.mainloop()
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Enter', command=self.hello)
        self.alertButton.pack()
        
            
        
    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
# 主消息循环:
app.mainloop()