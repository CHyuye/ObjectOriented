# 全局变量
title = "模块二"


# 函数
def say_hello():
    print("我是 %s" % title)


# 类
class Animal(object):
    pass


# print(__name__) 会直接输出 __main__
if __name__ == "__main__":

    print(__name__)
    print("Jake doing")