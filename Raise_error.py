# 异常
"""
    在程序运行时，如果python解释器遇到一个错误，会停止程序的执行，并且提示一些
    错误信息，这就是异常
    程序停止执行并且提示错误信息这个动作，通常称为：抛出异常
"""

# try:
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     print(result)
#
# except ZeroDivisionError:
#     print("除零错误！")
#
# # except ValueError:
# #     print("请输入正确的数字！")
#
# # 2、捕获未知错误，记住 —— 代码语句固定如下：
# except Exception as result:
#     print("未知错误 %s" % result)


# 3、异常捕获的完整语法

# try:
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     print(result)
#
# except ValueError:
#     print("请输入正确的数字")
#
# except Exception as result:
#     print("未知错误 %s" % result)
#
# # else 只有在异常时才会执行
# else:
#     print("该句代码，只有在没有异常时，才会执行")
#
# # finally 无论是否有异常都会执行
# finally:
#     print("该句代码，无论是否异常都会执行")


# 4、异常的传递
"""
    异常的传递 —— 当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方
    如果传递到主程序，仍然没有异常处理，程序才会终止
    
    提示：在开发中，可以在主函数增加异常捕获
"""

# def demo1():
#
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     return result
#
# def demo2():
#
#     return demo1()
#
#
# try:
#     print(demo2())
#
# except ValueError:
#     print("请输入正确的数字！")
#
# except Exception as result:
#     print("未知错误 %s " % result)
#
# finally:
#     print("异常的传递性")


# 5、主动抛出异常的应用场景
# 示例：提示用户输入密码，如果长度少于8，抛出异常
# 注意：当前函数负责提示用户输入密码，如果长度不够，有其他函数捕获异常

"""
    · python中提供一个Exception异常类
        1、创建一个Exception的对象
        2、使用raise关键字抛出异常对象
"""


def input_password():

    # 1、提示用户输入密码
    pwd = input("请输入密码(不少于8位数):")

    # 2、判断密码长度大于8，则返回
    if len(pwd) >= 8:
        return pwd

    # 3、小于8 就主动抛出异常
    print("主动抛出异常")

    # 1、创建一个Exception的对象 —— 可以使用错误信息字符串作为参数
    ex = Exception("密码长度少于8位数")

    # 2、使用raise关键字抛出异常对象
    raise ex


# 提示用户输出密码
try:
    print(input_password())

except Exception as result:
    print(result)
