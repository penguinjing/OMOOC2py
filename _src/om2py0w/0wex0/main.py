# -*- coding: utf-8 -*-
import os  # import a module os.py

def main():  # define a function call main()
    print 'Hello world!'

    print "This is Alice's greeting."
    print 'This is Bob\'s greeting.'

    foo(5, 10)  # call function foo() passing 2 variables (5, 10)

    print '=' * 10  # print 10 times of equal marks. asterisk = times
    print 'Current working direcotory is' + os.getcwd() 
    # call os.getcwd() method and join with print out string.


    counter = 0 # assign variable counter to 0
    counter += 1 
    # counter = counter + 1,  assign the result of counter + 1 back to variable counter.


    food = ['apples', 'oranges', 'cats']
    # assign the list ['apples', 'oranges', 'cats'] to name food.

    for i in food: # start a loop, assign the variable i though out list food.
        print 'I like to eat ' + i
        # print srting join with variable i result each loop.


    print 'Count to ten:'
    for i in range(10): # start a loop, assign the variable i from 0 to 9.
        print i # print the variable i result each loop.


def foo(param1, secondParam): 
#define a function call foo() with 2 parameter param1 & secondParmp

    res = param1 + secondParam 
    # assigne the sum of variable param1 plus secondParam to variable res.

    print '%s plus %s is equal to %s' % (param1, secondParam, res)
    # print param1 + ' plus ' + secondParam + ' is equal to ' + res

    if res < 50: # if res < 50, run following script print 'foo'
        print 'foo'

    elif (res >=50) and ((param1 == 42) or (secondParam == 24)):
        # then, else if the conditions are true, run following script.
        print 'bar'

    else: # finally, if all above conditions are false, run following script.
        print 'moo'

    return res # This is one-line comment. return the results of variable res back to the main() function.
    ''' A multi-
 line string, but can also be a multi-line comment.'''

if __name__ == '__main__': # if it's running in command line, run following script.
    main() # call main() function.
