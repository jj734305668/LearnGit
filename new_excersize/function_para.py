# _*_ coding:utf-8 _*_

"""
函数参数

位置参数：
def f(m ,n)

默认参数//必选参数在前，默认参数在后//默认参数不指向对象
def f(m ,n=2)

可变参数//参数数量可变//
def f(*params)
list = []
f(*list)

关键字参数：
允许出啊如dict
def f(**params)
f(city='nanjing', age=10)
dict = {}
f(**dict)
"""


def f1(*l):
    print(l)


def f2(**d):
    print(d)


l_list = [1, 2, 3, 4]
f1(l_list)
f1(*l_list)

d_dict = {'name': "x_h", 'age': 10}
# f2(d_dict)
f2(**d_dict)


# 若要限制关键字参数的名字
def f3(name, age, *, city, job):
    print(name, age, city, job)


# 或者函数中 有可变参数 则不需要使用*
# 若关键字参数无默认值，则必须填写关键字参数，否则被作为位置参数

def f4(name, age, *params, city, job):
    print(name, age, city, job)
