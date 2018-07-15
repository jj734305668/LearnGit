# _*_ coding:utf-8 _*_

"""
dict


"""
x_ming = {'name': 'x_ming', 'age': 15}
print(x_ming['name'])
#  避免key不存在
print('name' in x_ming)
print('age_' in x_ming)
# 或者使用get方法  key存在则返回对应的值 不存在返回none或指定返回值
print(x_ming.get('name'))
print(x_ming.get('age_', 1))
print(x_ming.get('age_'))
# 删除
x_ming.pop('name')
print(x_ming)

"""
set
集合
"""
ex_set = {1, 2, 3, 4}
print(ex_set)
ex_set = set({1, 2, 3, 4})
print(ex_set)
ex_set = set()
print(ex_set)
ex_set = {}
print(ex_set)
print(isinstance(ex_set, dict))
print(isinstance(ex_set, set))
