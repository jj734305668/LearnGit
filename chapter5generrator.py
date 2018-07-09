# _*_ coding:utf-8 _*_

""""
生成器-----是一个返回迭代器的函数

下面是一个用生成器实现的斐波那契函数实例

"""
import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+ b
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration :
        sys.exit()
