# -*- coding: utf-8 -*-
import os   #import a module os.py

def main():    #define a function call main()
    print 'Hello world!'

    print "This is Alice's greeting."
    print 'This is Bob\'s greeting.'

    foo(5, 10)

    print '=' * 10
    print 'Current working direcotory is' + os.getcwd()


    counter = 0
    counter += 1


    food = ['apples', 'oranges', 'cats']

    for i in food:
        print 'I like to eat ' + i


    print 'Count to ten:'
    for i in range(10):
        print i


def foo(param1, secondParam): 
#define a function call foo() with 2 parameter param1 & secondParmp

    res = param1 + secondParam

    print '%s plus %s is equal to %s' % (param1, secondParam, res)

    if res < 50:
        print 'foo'

    elif (res >=50) and ((param1 == 42) or (secondParam == 24)):
        print 'bar'

    else:
        print 'moo'

    return res # This is one-line comment.
    ''' A multi-
 line string, but can also be a multi-line comment.'''

if __name__ == '__main__':
    main()
