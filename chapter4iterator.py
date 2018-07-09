# _*_ coding:utf-8 _*_

"""
迭代器

适用于字符串、元组、列表
"""

list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = iter(list_test)
for temp in range(10):
    print(next(i), end=",")
for temp in i:
    print(temp, end="  ")
for temp in list_test:
    print(temp, end=".")


zz = [1, 2, 3, 4]
it = iter(list_test)    # 创建迭代器对象
for x in it:
    print(x, end=" ")

"""需要注意迭代器状态///不重复使用迭代器///需要使用的时候重新定义迭代器"""
