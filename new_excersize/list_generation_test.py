# _*_ coding:utf-8 _*_

"""

列表生成式
"""

print([x * x for x in range(1, 100, 5)])
print([m + n for m in 'abc' for n in 'xyz'])
l_list = ['fa', 2, 'sdfFFFFas', 4]
print([x.lower()for x in l_list if isinstance(x, str)])

