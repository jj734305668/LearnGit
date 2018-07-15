# _*_ coding:utf-8 _*_

"""
迭代器


Iterable 可迭代  可作用于for
Iterator 迭代器  可作用于iter()

"""
from typing import Iterator, Iterable

print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
