# _*_ coding:utf-8 _*_

"""
标准数据类型
    Number，String，List，Tuple，Set，Dictionary
    不可变数据：Number，String，Tuple
    可变数据：List，Set，Dictionary

    Number：int，float，bool，complex

    List:写在方括号之间，可以被索引，用+拼接，元素可以改变
    Tuple：写在小括号之间，可以被索引，用+拼接，不可被改变
    Set: 无序不重复元素序列/关系测试，删除重复元素/用{}或set()创建集合/创建空集合用set()而不是{}，{}是用来创建字典的
    dictionary:
"""

# import chapter3fibonacci.py

a, b, c, d = 1, 1.1, 1+1j, True
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

# 空元组
s = ()
# 一个元素
d = (1,)

# 空集合
zz = set()
# 成员测试
set_test = {"zzzz", 1, "zxc"}
if "1" in set_test:
    print("z")
else:
    print("x")

ad = set("ds")
sd = set("dsdadsadasd")
print(ad | sd)
print(ad - sd)
print(ad & sd)
print(ad ^ sd)
