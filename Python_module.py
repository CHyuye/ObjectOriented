# 一 —— 模块

# 1) 通过模块名，使用模块提供的工具 —— 全局变量，函数，类
# import python_TryModule1

# 2) 使用as指定模块别名 —— 大驼峰命名法
# import python_TryModule2 as Tm2

# 3) from···import
# 从什么模块导入某个工具
# from python_TryModule1 import say_hello
# 注意：如果两个模块，存在同名函数，那么后导入的模块函数会覆盖先导入的
# from python_TryModule2 import say_hello as Tm2_Function

# 4) 从模块中导入所有工具（正常不推荐使用，仅供知道）
# from python_TryModule1 import *

# print(Tm2.title)

# 注意：如果两个模块，存在同名函数，那么后导入的模块函数会覆盖先导入的
# 这时需要用别名 as关键字给一个工具起别名
# say_hello()
# Tm2_Function()


# 2、模块的搜索顺序(扩展)
"""
    1）搜索当前目录指定模块名的文件，如果有就直接引用
    2）如果没有，再搜索系统目录
    所以在开发时，给文件起名，不要和系统的文件重名，
    python解释器会加载当前目录下的同名文件
"""
# import random
#
# # python内置函数 __file__ 可以查看模块的完整路径
# print(random.__file__)
# print(random.randint(1, 10))


# 3、原则 —— 每个文件都应该可以被导入
"""
    · 一个独立的python文件就是一个模块
    · 在导入文件时，文件中所有没有任何缩进的代码都会被执行一遍
    
    ·开发场景 —— 仅在模块使用时，而被导入到其他文件中不会执行
"""
# import python_TryModule2
# import python_TryModule1
#
# print("-" * 50)


# 二 —— 包
"""
    包的概念：
    1、包是一个包含多个模块的特殊目录
    2、目录下有一个特殊的文件，__init__.py
        要在外界使用包中的模块，需要在__init__.py中指定
        对外界提供的模块列表
    3、包名的命名方式和变量名一样，小写字母+_
    
    好处：import 包名 可以一次性的导入保重所有的模块
"""
# 在外部直接导入包
import try_message

try_message.send_message.send("demo.py")

txt = try_message.receive_message.receive()
print(txt)
