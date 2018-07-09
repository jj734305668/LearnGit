# _*_ coding:utf-8 _*_

"""
函数

参数类型
必须参数、关键字参数、默认参数、不定长参数

匿名函数
"""


# 传不可变对象
def ex1(a):
    a += 10
    return a


# 传可变对象
def ex2(a):
    a[0] = 10


a = 20
ex1(a)
print(a)
a = [103, 20]
ex2(a)
print(a)


# 必须参数
def ex3(ex3_para):
    return ++ex3_para


print(ex3(19))


# 关键字参数
def ex4(name, age):
    print("mingzi:" + name + "---nianling:")
    print(age)


ex4(age=10, name="zzz")


# 默认参数
def ex5(name="zzzzzz"):
    print("sss" + name)


ex5()


# 不定长参数
def ex6(n, aa, *b):
    print(aa)
    print(b)
    print(n)


ex6(1, 2, 3, 4, 5, 676, 7, 8, 8, 9)


def ex7(n, **nn):
    print(n)
    print(nn)


ex7(1, a=2, b=3, c=4, d=5)


# 匿名函数
sum_i = lambda aa, bb: aa + bb

print(sum_i(1, 2))

# global 和 nonlocal关键字

