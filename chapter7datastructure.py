# _*_ coding:utf-8 _*_

"""
数据结构

列表推导式

"""

vec = (1, 2, 3)
vec2 = [3 * x for x in vec]
print(vec2)
vec3 = [[x, x*2] for x in vec]
print(vec3)
vec4 = [x*100 for x in vec if x > 2]
print(vec4)

vec5 = (
    (3, 45, 6, 423),
    (56, 67, 34, 43),
    (54, 465, 567, 65)
)
print(vec5)
for row in vec5:
    print(row[1])
vec6 = [row[1] for row in vec5]
print(vec6)
vec7 = [[row[i] for row in vec5] for i in range(4)]
print(vec7)


# del语句
