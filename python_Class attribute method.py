# 类的结构
# 1、术语 —— 实例
"""
    1、使用面向对象开发，第一步是设计类
    2、使用类名()创建对象，创建对象的两个步骤：
        1）在内存中为对象分配空间
        2）调用初始化方法 __init__()为对象初始化
    3、对象创建后，内存中就有了一个对象的实实在在的存在 —— 实例

    结论：
    · 每个对象都有自己的独立空间，保存各自不同的属性
    · 多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用传递到方法内部
"""

# 2、类是一个特殊的对象 —— python中一切皆是对象
"""
    · 在程序运行时，类同样会被加载到内存中
    · 类是一个特殊的对象 —— 类对象
    · 类对象在内存中只有一份，使用一个类可以创建出很多个对象实例
    · 除了封装实例的属性和方法外，类对象还可以有自己的属性和方法
        1、类属性：
        · 类属性是给类对象定义的属性
        · 用来记录这个类的相关特征
        · 类属性不会用于记录具体对象的特征
        
        2、类方法
    · 通过类名. 的方式可以访问类的属性或者调用类的方法
"""


# class Tool(object):
#
#     # 使用赋值语句，定义类属性，记录所有工具对象的数量
#     count = 0
#
#     def __init__(self, name):
#
#         # 对象的属性叫作 实例属性
#         self.name = name
#
#         # 针对类属性值 +1
#         Tool.count += 1
#
#     # 对象调用的方法叫作 实例方法
#     def work(self):
#
#         print("拿起 %s 去工作。" % self.name)
#
#
# # 创建出来的对象叫做 类的实例
# # 创建对象的动作叫作 实例化
# tool1 = Tool("榔头")
# tool2 = Tool("扳手")
# tool3 = Tool("改锥")
# tool1.work()
#
# # 访问类属性的两种方式
# # 输出工具类总数
# # 推荐使用第一种： 类名.类属性
# print("1.工具类总数 %d " % Tool.count)
#
# # 第二种不推荐
# # 注意：如果使用 对象.类属性 = 值 赋值语句，只会给对象添加一个属性，而不会影响到类属性
# tool1.count = 99
# print("2.工具类总数 %d" % tool1.count)


# 3、类方法 —— 就是针对类对象定义的方法，
# 在类方法内部可以直接访问类属性或者调用其他的类方法
"""
    类方法需要用修饰符 @classmethod 来标识
    类方法的第一个参数应该是 cls
    · 在通过类名，调用类方法，调用方法时，不需要传递cls参数
    · 在方法的内部：
        ·可以通过cls，访问类的属性
        ·也可以通过cls，调用其他的类方法
"""

# class Tool(object):
#
#     count = 0
#
#     @classmethod
#     def show_tool_count(cls):
#         print("工具的总数：%d " % cls.count)
#
#     def __init__(self, name):
#
#         self.name = name
#         # 类属性 +1
#         Tool.count += 1
#
#     def work(self):
#
#         print("拿着[%s]去工作。" % self.name)
#
#
# # 创建工具对象
# tool1 = Tool("榔头")
# tool2 = Tool("扳手")
# tool3 = Tool("改锥")
#
# # 调用类方法
# Tool.show_tool_count()


# 静态方法
# 静态方法开发场景：既不需要访问实例属性或者调用实例方法，
# 又不需要访问类属性和调用类方法时
# class Dog(object):
#
#     # 定义静态方法：需要用@staticmethod来标识
#     @staticmethod
#     def run():
#         print("小狗要跑··")
#
#
# # 静态方法的调用：类名.调用静态方法名
# Dog.run()


"""
    案例小结：
    1、实例方法 —— 方法内部需要访问实例属性
        · 实例方法内部可以使用 类名.访问类属性
    2、类方法 —— 方法内部只需要访问类属性
    3、静态方法 —— 方法内部，不需要访问类属性和实例属性
    
    如果方法内部既需要访问实例属性又需要访问类属性，应该定义成实例方法
"""


# 方法综合案例
class Game(object):

    # 定义一个类属性记录最高分
    top_score = 0

    # 定义一个实例属性，记录玩家姓名
    def __init__(self, player_name):

        self.player_name = player_name

    # 静态方法，显示帮助信息
    @staticmethod
    def show_help():
        print("阻止僵尸进入房间")

    # 类方法，显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("您当前最高成绩是:%d " % cls.top_score)

    # 实例方法，开始玩家游戏
    def start_game(self):
        print("%s 开始游戏···" % self.player_name)


# 1、查看游戏帮助
Game.show_help()

# 2、查看历史最高
Game.show_top_score()

# 3、创建游戏对象
game = Game("Allen")

game.start_game()

