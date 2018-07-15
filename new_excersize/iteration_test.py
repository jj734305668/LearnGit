# _*_ coding:utf-8 _*_

"""
迭代

"""
from typing import Iterable

# list


l_list = []
for i in range(20, 100, 5):
    l_list.append(i)
for i in l_list:
    print(i)
d_dict = {'a': 1, 'b': 2, 'c': 3}
# dict 迭代   根据key
for key in d_dict:
    print(key)
for value in d_dict.values():
    print(value)
for key, value in d_dict.items():
    print(key + ":" + str(value))

# 判断是否是可迭代对象, 若薇True则可以迭代

print(isinstance('a,b,c', Iterable))
