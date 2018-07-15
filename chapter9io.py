# _*_ coding:utf-8 _*_

"""
str():用户易读
repr():解释器易读
"""

s = "hello\n"

print(str(s))
print(repr(s))

for x in range(10):
    print(repr(x).rjust(1) + repr(x**2).rjust(3) + repr(x**3).rjust(5))

