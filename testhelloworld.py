# _*_ coding:utf-8 _*_

"""
基础语法

编码 默认

标识符：字母或下划线开始/数字字母下划线组成/大小写敏感

保留字  print(keyword.kwlist)

注释 #或者三个引号

行与缩进：python中使用缩进来表示代码块/同一代码块所有语句缩进行数必须相同

多行语句：语句过长，使用反斜杠实现多行语句/[],{},()中的多行语句，不需要使用\

数字类型：int,1/bool,true/float,1.23,3E-2/complex,1+2j

字符串：单双引号完全相同/三个引号指定多行字符/转义字符-反斜杠/字符串前加‘r’，不转义/右面从-1开始索引/左面从0开始索引/字符串不能改变/没有单独的字符类型，字符即长度为一的字符串

用户输入：input()

同一行显示多条语句：分号隔开

print实现不换行：变量末尾加上end=""

"""
import keyword

print(keyword.kwlist)

i = 1 + \
    2
print(i)

print(r'\/n')

# 字符串截取
s = 'this is a string!'
print("1:" + s)
print("2:" + s[0:1])
print("3:" + s[0:-1])
print("4:" + s[2:6])
print("5:" + s[3:0])
# print("6:" + s[-1:2])
print("7:" + s * 2)

a = input("轻松输入：")
print(a)

print(s, end=" ")
print(a, end=" ")
