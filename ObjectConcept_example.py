# 面向对象封装案例
"""
    封装
    1、封装是面向对象编程的一大特点
    2、面向对象编程的第一步 —— 将属性和方法封装到一个抽象的类中
    3、外界使用类创建的对象，然后让对象去调用方法
    4、对象方法的细节都被封装到类的内部
"""

# 案例一 —— 小明爱跑步

# class Person:
#
#     def __init__(self, new_name, new_weight):
#
#         # self.属性 = 形参
#         self.name = new_name
#         self.weight = new_weight
#
#     def __str__(self):
#         return "我的名字叫 %s，体重 %.2f公斤" % (self.name, self.weight)
#
#     def eat(self):
#         print("%s 是吃货，吃完这顿再减肥" % self.name)
#         self.weight += 1
#
#     def run(self):
#         print("%s 爱跑步，跑步，锻炼身体好" % self.name)
#         self.weight -= 0.5
#
#
# # 提示： 在对象的方法内部，是可以直接访问对象的属性的！
# xiaoming = Person("小明", 60.0)
#
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)
#
# # 多个对象之间互不干扰
# xiaomei = Person("小美", 45.0)
#
# xiaomei.run()
# xiaomei.run()
# print(xiaomei)


# 案例二 —— 摆放家具

# class HouseItem:
#
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "[%s] 占地 %.2f平方米" % (self.name, self.area)
#
#
# class House:
#
#     def __init__(self, house_type, total_area):
#
#         self.house_type = house_type
#         self.total_area = total_area
#
#         # 剩余面积
#         self.free_area = total_area
#
#         # 家具名称列表
#         self.house_list = []
#
#     def __str__(self):
#
#         return ("户型:%s\n总面积:%.2f平方米(剩余面积:%.2f平方米)\n家具名称:%s"
#                 % (self.house_type, self.total_area,
#                    self.free_area, self.house_list))
#
#     def add_item(self, item):
#
#         # 1.判断家具的面积是否超过总面积
#         if item.area > self.free_area:
#             print("%s 的面积太大，无法添加！" % item.name)
#             return
#
#         # 2.将家具的名称添加到家具列表中
#         self.house_list.append(item.name)
#
#         # 3.计算剩余面积
#         self.free_area -= item.area
#
#
# # 创建家具
# bear = HouseItem("席梦思", 50)
# chest = HouseItem("衣柜", 40)
# table = HouseItem("书桌", 3)
#
# print(bear)
# print(chest)
# print(table)
#
# # 创建房子对象
# house = House("两室一厅", 60)
#
# house.add_item(bear)
# house.add_item(chest)
# house.add_item(table)
#
# print(house)


# 案例三 —— 士兵突击

class Gun:

    def __init__(self, model):
        # 枪型号
        self.model = model
        # 枪子弹数
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1、判断是否有子弹
        if self.bullet_count <= 0:
            print("[%s] 没子弹啊···" % self.model)

            return

        # 2、每发射一次减少
        self.bullet_count -= 1
        print("%s 突突突··· [%d]" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):

        self.name = name
        # 假设新兵没有枪
        self.gun = None

    def __str__(self):

        return "为人名服务 -- %s" % self.name

    def fire(self):

        # 1.判断士兵是否有枪
        # 针对None比较时，应该用 is 身份运算符
        if self.gun is None:
            print("[%s] 还没有枪···" % self.name)
            return

        # 2.喊一声口号
        print("冲啊··· [%s]" % self.name)

        # 3.装填子弹
        self.gun.add_bullet(40)

        # 4.开枪
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullet(40)
# ak47.shoot()

# 创建士兵对象
xusanduo = Soldier("许三多")
# 让许三多拿到枪
xusanduo.gun = ak47
# 许三多开火
xusanduo.fire()
print(xusanduo)


# 4 、、python的身份运算符 is 和 is not
# 身份运算符用于比较两个对象的内存地址是否一致 —— 是否是对同一个对象引用

# is 和 == 的区别
# is用于判断两个变量引用的对象是否为同一个
# == 用于判断是否为同一个值


class Woman:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    # 定义私有属性和方法： 在属性和方法前加 '__'
    # 私有属性私有方法，是不希望对外公开的属性和方法
    def __secret(self):

        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s age is %d." % (self.name, self.__age))


Allen = Woman("Allen")

# 私有属性不允许外界直接访问
# python处理私有属性访问： 使用 _类名__属性，可以访问到
print(Allen._Woman__age)  # 日常开发时，不能使用这种方式去访问私有属性与方法

# 私有方法同样不允许外界访问
# python处理私有方法访问： 使用 _类名__方法名，可以访问到
Allen._Woman__secret()