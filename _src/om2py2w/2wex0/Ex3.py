# -*- encoding: utf-8 -*-
"""
Created on Thu Apr 28 11:53:22 2011

@author: He Jibo
hejibo@ueseo.org
University of Illinois

function:
    a workable program for creating new contacts
    for use of our  Real Python bookchpater

    
"""

import Tkinter

FILENAME = "addressfile.txt"


def save_file(self):
    '''
    保存数据到文件
    '''
    text_file = open(FILENAME,"a")
    first = self.txtfirst.get().encode("utf-8")#http://flyantme.blog.163.com/blog/static/7586977520096711026111/
    last = self.txtlast.get().encode("utf-8")
    address = self.txtadd.get().encode("utf-8")
    city = self.txtcity.get().encode("utf-8")
    state = self.txtst.get().encode("utf-8")
    zipcode = self.txtzip.get().encode("utf-8")
    phone = self.txtph.get().encode("utf-8")
    email = self.txtemail.get().encode("utf-8")
    print >>text_file,last,"\t",first,"\t",address,"\t",city,"\t",state,"\t",zipcode,"\t",phone,"\t",email
    text_file.close()
    self.win.destroy()


root = Tkinter.Tk()
#设置软件尺寸
root.geometry("400x230+100+100")
d = Tkinter.Frame(root)


#名
txtfirst = Tkinter.Entry(d, width = 40)
fname = Tkinter.Label(d, width = 15,text = u"名")
fname.pack(side = "left",pady = 8)
txtfirst.pack(side = "left")
d.pack(side = "top",fill = "x")

#姓
e = Tkinter.Frame(root)
txtlast = Tkinter.Entry(e, width = 40)
lname = Tkinter.Label(e, width = 15,text = u"姓")
lname.pack(side = "left",pady = 8)
txtlast.pack(side = "left")
e.pack(side = "top",fill = "x")

#街道
f = Tkinter.Frame(root)
txtadd = Tkinter.Entry(f, width = 40)
address = Tkinter.Label(f, width = 15,text = u"街道")
address.pack(side = "left",pady = 8)
txtadd.pack(side = "left")
f.pack(side = "top",fill = "x")

#市
g = Tkinter.Frame(root)
txtcity = Tkinter.Entry(g, width = 16)
city = Tkinter.Label(g, width = 15,text = u"市")
city.pack(side = "left",pady = 8)
txtcity.pack(side = "left")

#省
txtst = Tkinter.Entry(g, width = 4)
street = Tkinter.Label(g, width = 8,text = u"省")
street.pack(side = "left",pady = 8)
txtst.pack(side = "left")

#邮政编码
txtzip = Tkinter.Entry(g, width = 8)
zipcde = Tkinter.Label(g, width = 8,text = u"邮政编码")
zipcde.pack(side = "left",pady = 8)
txtzip.pack(side = "left")
g.pack(side = "top",fill = "x")

#电话
h = Tkinter.Frame(root)
txtph = Tkinter.Entry(h, width=16)
phone=Tkinter.Label(h, width = 15,text = u"电话")
phone.pack(side = "left",pady = 5)
txtph.pack(side = "left")

#电子邮箱
txtemail = Tkinter.Entry(h, width = 16)
email = Tkinter.Label(h, width = 10,text = "E-mail")
email.pack(side = "left",pady = 8)
txtemail.pack(side = "left")
h.pack(side = "top",fill = "x")
j = Tkinter.Frame(root)
j.pack(side = "left",fill = "y")

#保存按钮
save = Tkinter.Button(j, text = u"保存")
save.pack(pady = 20, padx = 10)    
i = Tkinter.Frame(root)
i.pack(side = "top",fill = "x")

#取消按钮
close = Tkinter.Button(i, text = u"取消",command = root.destroy)
close.pack(side = "right",pady = 10, padx = 75)

root.mainloop()