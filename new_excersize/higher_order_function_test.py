# _*_ coding:utf-8 _*_

"""

高阶函数


变量可以指向函数

"""

# 变量可以指向函数
print(abs)
f = abs
print(f)
print(f(-1))
# 函数名也是变量


# print(abs)
# abs = 10
# print(abs)


# 高阶函数


def func1(x, y, f):
    return f(x) + f(y)


print(func1(-1, -10, abs))

