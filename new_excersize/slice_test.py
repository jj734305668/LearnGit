# _*_ coding:utf-8 _*_

"""
切片

字符串操作
"""

l_list = [1, 2, 3, 4, 5]
print(l_list[0: 5])
print(l_list[0: -1])
print(l_list[-3: -1])

# 每隔n个取一个

for x in range(10, 100, 5):
    l_list.append(x)

print(l_list)
print(l_list[: 10: 3])
