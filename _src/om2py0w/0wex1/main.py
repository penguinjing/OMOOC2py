# -*- coding: utf-8 -*-
from sys import argv

line = ''

fhand = open(argv[1], 'r+')

print 'Here are the dairy lines that you already wrote:'
print fhand.read()

print 'Please input your dairy here: '
print 'Type "finish" in a new line if you are done. '

while True:
    line = raw_input('> ')
    if line == 'finish':
        break
    fhand.seek(0, 2)
    fhand.write(line + '\n')

print 'The dairy was saved. Thanks for using Mini Dairy Writer.'
fhand.close()