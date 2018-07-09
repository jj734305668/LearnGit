# _*_ conding:utf-8 _*_

"""

模块
"""


def fib(n):
    a, b = 0, 1
    while b < n:
        print(a)
        a, b = b, a + b


def fib2(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    print("m1----------------main")
else:
    print("m1----------------not main")
