# _*_ coding:utf-8 _*_

"""
list
初始化：中括号
访问：索引（从0开始，超出范围--》IndexError）



"""

ex_list = ["a", "b"]
# 访问
print(ex_list[-1])
# 追加
ex_list.append("a")
print(ex_list)
# 插入 序号从0开始
ex_list.insert(0, "sas")
print(ex_list)
# 删除
ex_list.pop()
print(ex_list)
ex_list.pop(0)
print(ex_list)
# 替换
ex_list[1] = "v"
print(ex_list)

"""
tuple 
定义：小括号

"""
ex_tuple = ()
print(ex_tuple)
ex_tuple = (1,)
print(ex_tuple)

