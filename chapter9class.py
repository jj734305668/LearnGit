# _*_ coding:utf-8 _*_

"""
类
"""

class People:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.age = a
        self.name = n
        self.__weight = w

    def speak(self):
        print("%s说：我%d岁,%d公斤重" % (self.name, self.age, self.__weight))


# 单列继承
class Student(People):
    grade = 0

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        People.speak(self)
        print(str(self.grade) + "年级")


if __name__ == "__main__":
    s = Student("XiMing", 10, 200, 1)
    s.speak()
else:
    print("a")
