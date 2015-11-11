# -*- coding: UTF-8 -*-*
'''
# 单一窗口，2按钮，'Quit' + 'Hello'(按下后Python解释器显示：hi there, everyone!)
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
'''
'''
# 单一窗口，1按钮，'Quit'
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Mini Diary Writer')
app.mainloop()
'''
'''
# 单一窗口，1 Label控件，显示Hello World 
from Tkinter import *

root = Tk()

label = Label(root, text = 'Hello World')
label.pack()
root.mainloop()
'''
# Hello world - 1
#import Tkinter
#top = Tkinter.Tk()

#top.mainloop()
'''
# 单一窗口，2 List控件，显示2列表内容。
from Tkinter import *
root = Tk()

li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)

listb.pack()
listb2.pack()
root.mainloop()
'''
'''
from os.path import exists

def print_all_records(f):
    line_count = 1
    print 'Previous dairy records: \n'
    for current_line in f:
        print '%i - %s' % (line_count, current_line[:-1])
        line_count +=1 # line = line + 1
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
        
    current_file.close()

if __name__ == '__main__':
    main()

'''

from os.path import exists
import Tkinter as tk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_all_records(f):
    content = 'All previous records: \n'
    for current_line in f:
        content = content + current_line[:-1] + '\n'
    return content

def save(f): 
    f.write(line + '\n')

def main():

    log_name = 'mydairy.log'
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

    content_input = tk.StringVar()

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

if __name__ == '__main__':
    main()
