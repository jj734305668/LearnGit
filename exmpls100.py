# _*_ coding:utf-8 _*_

"""
100个python实例
"""
import cmath
import random


def py_ex_sum():
    print("两数之和为：%.3f" % (float(input("请输入第一个数字：")) + float(input("请输入第二个数字："))))


def py_ex_sqrt():
    num = float(input("请输入一个数字："))
    if num >= 0:
        print("{0}的平方根是{1:.3f}".format(num, num ** 0.5))
    else:
        num_sqrt = cmath.sqrt(num)
        print("{}的平方根是{}+{}j".format(num, num_sqrt.real, num_sqrt.imag))


if __name__ == "__main__":
    # py_ex_sum()
    # py_ex_sqrt()
    print(random.randint(0, 100))
else:
    print("非main")
