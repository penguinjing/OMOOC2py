# -*- coding: utf-8 -*_
import os
print "历史日志："
#请先忽略文件路径，稍后再改
if os.path.exists('/Users/sean/Documents/python/1.txt'):
	duqu = open('1.txt')
	print duqu.read()
	duqu.close()

else:
	print "现在开始写下你的第一行日志:"

while 1 > 0:
	diary = open('1.txt', 'a')
	line = raw_input("请输入：")
	if line == 'quit' or line == 'q':
		break
	elif line == '?' or line =='h' or line =='help':
		print "若想结束程序，请输入'q'或者'quit'."
	else:
		diary.write(line +'\n')
	diary.close()