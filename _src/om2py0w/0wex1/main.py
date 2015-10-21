# -*- coding: utf-8 -*-
from sys import argv

line = ''

try: 
    fname = open(argv[1], 'a')
    print fname.read()

except:
	fname = open(argv[1], 'w')

print 'Please input your dairy here: '
print 'Type "finish" in a new line if you are done. '

while True:
    line = raw_input('> ')
    if line == 'finish':
    	break
    fname.write('%s \n'), line

print 'Ok, done. The dairy was saved. Thanks for using the mini dairy writer.'
fname.close()