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