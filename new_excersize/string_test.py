# _*_ coding:utf-8 _*_

"""
字符串和编码

ascii编码：一个字节表示一个字符
unicode：大部分两个字节表示一个字符
utf-8：变长字节

计算机内存中都使用unicode方式

文件读取到内存中  utf-8----》unicode
内存保存到文件中  unicode-----》utf-8

"""

__author__ = "jia_jie"

s = "this is a string !!-----这是一个字符串 ！！"
s_byte_utf8 = s.encode("utf-8")
s_byte_unicode = s.encode("utf-16")
print(s_byte_utf8)
print(s_byte_unicode)
print("s.length:%d\ns_byte_utf8.length:%d\ns_byte_unicode.length:%d" % (len(s), len(s_byte_utf8), len(s_byte_unicode)))
