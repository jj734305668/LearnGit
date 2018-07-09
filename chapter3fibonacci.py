# _*_ coding:utf-8 _*_

"""
斐波那契队列
"""
a, b = 0, 1
while b < 50:
    print(a)
    a, b = b, a + b
