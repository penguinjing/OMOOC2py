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

# 本程序片段使用的程序方法
# 1. 导入其他模块 - import os 系统模块(os.py)
# 2. 构造了两个函数 main() - 无参数函数, foo() - 2参数函数.
# 3. 运行时检测程序状态：a. 由其他程序导入调用，还是b. 直接运行.
# 4. main()运行内部，可调用第二个函数foo(). 调用函数时可传递参数进入函数foo(param1, secondParam)
# 5. 使用列表(List)前定义列表, 循环条件for i in food:使用列表作为循环参数。
# 6. 使用函数range(10), 构造列表(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),  把for i in range(10)，作为循环条件。
# 7. 调用os模块方法，os.getcwd() getCurrentWorkingDirectory
# 8. 条件判断 if - elif - else。 函数返回值在函数末尾return.
# 9. 格式化字符串