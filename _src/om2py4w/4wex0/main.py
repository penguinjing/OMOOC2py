# -*- encoding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明： Web版的极简交互式笔记程序
作者信息： penguinjing
版本自述:  0.0.1
程序参考： None
'''
# 全局引用
from bottle import route, run, template

# 全局变量
# PATH = "/path/2/work dir"
# 函式撰写区

#from bottle import route, run, template
@route('/')
@route('/hello/<name>')
def index(name='Stranger'):
    return template('<b>Hello {{name}}, how are you? </b>!'
                    , name=name)

run(host='localhost', port=8080)