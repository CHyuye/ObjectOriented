# 面向对象编程 —— 继承: 子类拥有父类的所有属性和方法
"""
    面向对象三大特点
    1、封装 —— 根据职责将属性和方法封装到一个抽象的类中
    2、继承 —— 实现代码的重用，相同的代码不用重复的编写
    3、多态 —— 不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
"""

# 继承的概念：子类拥有父类的所有属性和方法
# 专业术语：Dog类是Animal的派生类，Animal是Dog类的基类，Dog从Animal类中派生
# 1、单继承
# class Animal:
#
#     def eat(self):
#         print("吃--")
#
#     def drink(self):
#         print("喝--")
#
#     def run(self):
#         print("跑--")
#
#     def sleep(self):
#         print("睡--")
#
#
# # 继承语法： class 类名(父类名)
# class Dog(Animal):
#
#     def bark(self):
#         print("汪汪叫")
#
#
# # 子类拥有父类以及父类的父类中封装的所有属性和方法
# class xiaotianquan(Dog):
#
#     def fly(self):
#         print("我会飞")
#
# # 创建狗对象
# wangcai = Dog()
# wangcai.run()
# wangcai.bark()
#
# # 创建哮天犬的对象
#
# xtq = xiaotianquan()
#
# xtq.fly()
# xtq.sleep()


# 2、方法的重写
"""
    当父类的方法实现不能满足子类的需求时，可以对方法进行重写
    重写后，在运行时，只会调用子类中的重写的方法，而不再会调用父类封装的方法
    
    重写的两种情况：
    1、覆盖父类的方法
    2、对父类的方法进行扩展
"""


# class A:
#
#     def __init__(self):
#
#         self.num1 = 100
#         # 父类中的私有属性
#         self.__num2 = 200
#
#     # 父类中的私有方法
#     def __test(self):
#         print("父类中的私有方法 %d[公有属性] %d[私有属性]" % (self.num1, self.__num2))
#
#     # 父类中的公有属性 —— 将私有属性和私有方法写入公有方法中，
#     # 子类就可以通过父类的公有方法间接访问到私有属性和方法
#     def test(self):
#         print("父类中的公有方法 %d[公有属性] %d[私有属性] " % (self.num1, self.__num2))
#
#         self.__test()
#
#     def write(self):
#         print("I can write English.")
#
#     def speak(self):
#         print("I can speak English.")
#
#
# class B(A):
#
#     def write(self):
#
#         # 1、覆盖 —— 在子类中重新编写父类的方法实现
#         print("I want write Chain.")
#
#         # 2、扩展 —— 子类的方法实现中需要父类的方法实现
#         # 扩展方法: super().父类方法名 调用父类的方法执行
#         super().write()
#
#         # 第二种扩展方法 适用于python2.x
#         # 父类名.方法名(self)
#         # A.write(self)
#         # 注意：如果使用子类调用方法，会出现递归导致死循环
#         # B.write(self)  # 特别注意不应该出现调用自己情况
#
#         # 3、或者编写子类特有的代码实现
#         print("I Love You")
#
#     def demo(self):
#
#         # 1、在子类的对象方法中，不能访问父类中的私有属性
#         # print("访问父类的私有属性 %d " % self.__num2)
#
#         # 2、不能调用父类的私有方法
#         # self.__test()
#
#         # 3、访问父类中的公有属性
#         print("子类方法访问父类公有属性 %d " % self.num1)
#
#         # 4、访问父类中的公有方法
#         self.test()
#
#
# people = B()
# print(people)
# people.write()
# people.demo()


# 3、多继承 —— 子类可以拥有多个父类，并且具有父类的属性和方法

# 多继承的新式类和旧式类
"""
    新式类: 以object为基类的类，就是新式类
    旧式类: 不以object为基类的类，是旧式类
    在python3.x中，创建类不指名object，默认会以object为基类
    python2.x中，需要指定object为父类继承
    建议：如果没有父类，统一继承自object
"""
# class A(object):
#
#     def test(self):
#
#         print("A -- test 方法")
#
#     def demo(self):
#
#         print("A -- demo 方法")
#
#
# class B(object):
#
#     def test(self):
#
#         print("B -- test 方法")
#
#     def demo(self):
#
#         print("B -- demo 方法")
#
#
# class C(A, B):
#
#     # 多继承可以让子类对象，同时拥有多个父类的方法和属性
#     pass
#
#
# c = C()
# # 现在A B 类中都有demo方法 test方法，在开发时应该避免这种混淆，尽量不使用多继承
# c.demo()
# c.test()
#
# # python中的 MRO —— 方法搜索顺序
# print(C.__mro__)


# 4、多态 —— 不同的子类对象调用相同的父类方法，产生不同的执行结果
"""
    1、多态可以增加代码的灵活度
    2、一继承和重写父类的方法为前提
    3、是调用方法的技巧，不会影响到类的内部设计
"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍···" % self.name)


class XiaotianDog(Dog):

    def game(self):
        print("%s 飞在天上玩耍···" % self.name)


class Person(object):

    def __init__(self, name):

        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩耍···" % (self.name, dog.name))

        dog.game()


# 创建狗对象
# wangcai = Dog("旺财")

# 创建子类 哮天犬， 多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
xtq = XiaotianDog("哮天犬")

# 创建小明
xiaoming = Person("小明")

xiaoming.game_with_dog(xtq)
print(Person.__mro__)
