# 面向对象编程
"""
    面向对象概念
    1、类，
    类是模板，对象是根据类这个模板创建出来的，先有类，再有对象
    类只有一个，而对象有很多个，不同的对象之间属性可能不同
    类中定义了什么属性和方法，对象中就有什么属性和方法，不可多或少


    2、程序设计一个类，通常要满足三个要素：
    （1）类名，这类事物的名字，满足大驼峰命名法（CapWords）每个单词大写，无下划线
    （2）属性，这类事物具有什么样的特征
    （3）方法，这类事物具有什么样的行为
    提示：需求中没有涉及的属性或者方法在设计类时，不需要考虑
"""


# 面向对象基础语法
"""
    目标
    1.dir内置函数
    2.定义简单的类
    3.方法中的self参数
    4.初始化方法
    5.内置方法和属性
"""

# 1、dir内置函数查询对象的方法列表
# python中的对象无处不在，变量，数据，函数都是对象
"""
    使用dir函数，传入标识符/数据，可以查看对向内的所有属性和方法
    提示：__方法名__ 格式的方法是python提供的内置方法/属性
"""


# 2、定义一个面向对象程序 —— 符合引用概念
# 需要：小猫爱吃鱼，小猫爱喝
# class Cat:
#
#     # 哪个对象调用的方法，方法内的self就是哪个对象的引用
#     # 在类封装的方法内部，self 就表示当前的调用方法的对象自己
#     # 在方法内部：可以通过self. 访问对象的属性，也可以self. 调用其他的对象方法
#
#     def eat(self):
#         print("{} like flash.".format(self.name))
#
#     def drink(self):
#         print("%s need drink." % self.name)
#
#
# 3、 创建猫对象
# tom_cat = Cat()
#
# # 在类的外部给对象增加属性 —— 可以用 .属性名 利用赋值语句就可以了
# # 注意：这种方式虽然简单，但是不推荐使用
# # tom_cat.name = "Tom Cat"
#
# tom_cat.eat()
# tom_cat.drink()
#
# 4、 在类的外部给对象增加属性，没有找到属性会报错，不推荐使用
# # AttributeError: 'Cat' object has no attribute 'name'
# tom_cat.name = "Tom"
#
# 5、 提示：在计算机中，通常用16进制表示内存地址
# print(tom_cat)  # 输出这个变量引用的对象，由那个类创建，以及内存的地址(十六进制)
#
# # addr = id(tom_cat)
# # print("%d" % addr)  # %d 可以以十进制输出数字
# # print("%x" % addr)  # %x 可以以十六进制输出数字
#
# # 创建另一个猫对象
# lazy_cat = Cat()
#
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
# lazy_cat.drink()
# print(lazy_cat)

# 引用的类内存地址完全相同是同一只猫
# lazy_cat1 = lazy_cat
# print(lazy_cat1)


# 6、初始化方法
"""
    当使用类名创建对象时，会自动执行以下操作：
    1、为对象在内存中分配空间 —— 创建对象
    2、为对象的属性设置初始值 —— 初始化方法(__init__)
"""
# class Cat:
#
#     # __init__ 方法是专门用来定义一个类具有哪些属性的方法
#     def __init__(self, new_name):
#
#         print("初始化方法！")
#         # self.属性名 = 属性初始值
#         # self.name = "Tom"
#
#         # 改造初始化方法 —— 初始化的同时设置初始值
#         # 在方法内部使用 self.属性 = 实参 接受外部传递的参数
#         self.name = new_name
#
#     def eat(self):
#
#         print("{} like flash.".format(self.name))
#
#     def drink(self):
#
#         print("{} need drink.".format(self.name))
#
#
# # 使用类名()创建对象时，会自动调用初始化方法(__init__)
# Tom = Cat("Tom")  # 创建对象时，输入实参 类名(属性1,属性2 ··)调用
# Tom.drink()
# Tom.eat()
# print(Tom.name)


# 7、 __del__ 方法
"""
    当使用类名() 创建对象时，为对象分配内存空间，自动调动 __init__方法
    当一个对象被从内存中销毁前，会自动调用 __del__ 方法
"""

# class Cat:
#
#     def __init__(self, new_name):
#
#         self.name = new_name
#
#         print("%s I coming." % self.name)
#
#     def __del__(self):
#
#         print("%s I leave." % self.name)
#
#
# # tom是一个全局变量
# tom = Cat("Tom")
# print(tom.name)
#
# # del 关键字可以删除一个对象
# del tom
#
# print("-" * 30)


# 8、 __str__ 方法
"""
    如果在开发时，希望使用print输出对象的变量时，能够打印自定义的内容，就可以
    使用__str__方法
    注意： __str__ 方法必须返回一个字符串
"""
class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s I coming." % self.name)

    def __del__(self):

        print("%s I leave." % self.name)

    def __str__(self):
        # __str__ 方法必须返回一个字符串
        return "I am %s cat." % self.name


tom = Cat("Tom")
print(tom)

lazy_cat = Cat("lazy cat")
print(lazy_cat)