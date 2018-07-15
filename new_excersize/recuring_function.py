# _*_ coding:utf-8 _*_

"""
递归函数

尾递归函数
当return语句的递归调用发现----》返回时没有任何事情可做的时候，
那么久没有保存栈帧的必要了
"""


def fibonacci_func(n):
    if n == 1:
        return 1
    else:
        return n + fibonacci_func(n-1)


def func2(n):
    return func3(0, n)


def func3(m, n):
    if n == 0:
        return m
    else:
        print("%d + %d, %d" % (m, n, n - 1))
        return func3(m + n, n - 1)


print(func2(10))

