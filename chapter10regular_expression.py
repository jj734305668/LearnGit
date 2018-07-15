# _*_ coding:utf-8 _*_

"""
正则表达式
"""
import re

re_mobile_phone = re.compile(r"(1)([3-9])([0-9]{9})")
print(re.match(re_mobile_phone, "18451544316").groups())
print(re.match(re_mobile_phone, "18261635266"))
print(re.match(re_mobile_phone, "1845154431"))



