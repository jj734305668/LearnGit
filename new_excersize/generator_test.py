# _*_ coding:utf-8 *_


"""
生成器
"""

# 注意
from typing import Iterable

a, b = 0, 1
a, b = b, a + b
print(a, b)
# 相当于
a, b = 0, 1
t = (b, a + b)
a, b = t[0], t[1]
print(a, b)

# 可以将    列表生成式 修改为  生成器

l_list = [x for x in range(0, 100, 5)]
print(l_list)
g_generator = (x for x in range(0, 100, 5))
print(g_generator)
print(next(g_generator))
print(next(g_generator))


# yield关键字定义生成器
# fibonacci
def fibonacci_func(max):
    n, a, b = 1, 0, 1
    while n < max:
        n += 1
        a, b = b, a + b
        yield b
    return 'done'


try:
    for n in fibonacci_func(10):
        print(n)
except StopIteration as e:
    print(e.value)

print(isinstance(fibonacci_func(10), Iterable))
