# -*- encoding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明： Web版的极简交互式笔记程序
作者信息： penguinjing
版本自述:  0.1.0
程序参考： None
'''
# 全局引用
from bottle import request, route, run, template
from time import localtime, strftime

# 全局变量
# PATH = "/path/2/work dir"
# 函式撰写区
def read_diary():
    f = open('diary log.txt','r')
    return f.read()

def write_diary(newdiary):
    f = open('diary log.txt','a+')
    edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
    f.write('%s    %s\n' % (edit_time, newdiary))
    f.close()

@route('/')
def start():
    log = read_diary()
    return template("diaryweb", diarylog=log)

@route('/', method='POST')
def input_new():
    newdiary = request.forms.get('newdiary')
    write_diary(newdiary)
    log = read_diary()
    return template("diaryweb", diarylog=log)


if __name__ == '__main__':
    run(host='localhost', port=8255, debug=True, reloader=True)