# 全局变量，函数，类，注意：直接执行的代码不是向外界提供的工具
# 全局变量
title = "模块一"


# 函数
def say_hello():

    print("我是 %s" % title)


# 类
class Animal(object):
    pass


print(__name__)  # 会直接输出 __main__
if __name__ == "__main__":

    # 文件被导入时，能过直接执行的代码不需要被执行
    print("Allen开发的文件")
    say_hello()
