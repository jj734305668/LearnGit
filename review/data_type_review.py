# _*_ coding:utf-8 _*_

"""
数据类型

python基本数据类型：数字/字符串/元组--------------------------------》不可变
                    列表/字典/集合----------------------------------》可变

Number:int,float,bool,complex
type()函数和isinstance()函数区别

int
float
string 转义字符 用\  或者 r

bool or and not 运算



空值 None


list
有序
索引/越界IndexError/-1
追加/append
删除/pop()/pop(i)

tuple
有序不可变
空/t = ()
一个元素/t = (1,)


diction
get()
pop()

set
无序不重复
add()
remove()




切片操作//list/tuple/string

迭代//for in //适用于一切可迭代对象Iterable

列表生成式
list()
[x表达式 for x in 范围 if 判断]

generator
列表生成器
带yield的函数

Iterator
iter(可迭代对象)

可作用于for in
可迭代对象
迭代器-》生成器/



                    |~~~~~可迭代对象list,tuple,string
可作用于for in------
                    |____迭代器（迭代器对象）————------iter(可迭代对象)
                                            |_____生成器------------------列表生成式改造
                                                               |__________带yield的函数


"""
from typing import Iterable, Iterator


class A:
    def a(self):
        return


class B(A):
    def a(self):
        return 'a'


class C(A):
    def a(self):
        return 'a'


print(type(A()) == A)
print(type(B()) == A)
print(isinstance(A(), A))
print(isinstance(B(), A))
print(isinstance(C(), A))
print(isinstance(Iterator, Iterable))
print(isinstance({}, Iterable))
