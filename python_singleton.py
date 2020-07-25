# 单例
# 单例设计模式
"""
    目的 —— 让类创建的对象，在系统中只有唯一的一个实例
    每一次执行 类名()返回的对象，内存地址是相同的
"""

# 1、__new__ 方法
"""
    __new__ 方法是由object积累提供的内置的静态方法，主要作用是：
        · 1）在内存对象中分配空间
        · 2）返回对象的引用
    · python的解释器获取对象的引用后，将引用作为第一参数，传递给 __init__
    
"""
# 2、重写__new__ 方法
"""
    1、重写 __new__ 方法一定要 return super().__new__(cls)
    否则python解释器得不到分配空间的引用，就不会调用对象的初始化方法
    2、注意：__new__方法是一个静态方法，在调用时需要主动传递cls参数
"""
# class MusicPlayer(object):
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1、创建对象时，new方法会被自动调用
#         print("创建对象，分配空间")
#
#         # 2、为对象分配空间
#         # 注意：__new__方法是一个静态方法，在调用时需要主动传递cls参数
#         instance = super().__new__(cls)
#
#         # 3、返回对象的引用
#         return instance
#
#     def __init__(self):
#
#         print("播放器初始化·")
#
#
# player = MusicPlayer()
#
# print(player)


# 3、python中的单例
"""
    · 定义一个类属性，初始值是None，用于记录单例对象的引用
    · 重写 __new__ 方法
    · 如果类属性 is None,调用父类方法分配空间，并在类属性中记录单例对象的引用
    · 返回类属性中记录的对象引用
"""


# class MusicPlay(object):
#
#     # 定义一个类属性，初始值是None，用于记录单例对象的引用
#     instance = None
#
#     # 重写 __new__ 方法
#     def __new__(cls, *args, **kwargs):
#
#         # 判断类属性是否为空对象
#         if cls.instance is None:
#             # 调用父类的方法为第一个对象分配方法
#             cls.instance = super().__new__(cls)
#
#         # 返回类属性保存的对象引用
#         return cls.instance
#
#
# # 创建多个对象
# play1 = MusicPlay()
# print(play1)
#
# play2 = MusicPlay()
# print(play2)


# 需求：只执行一次初始化工作
"""
    · 定义一个类属性 init_flag，标记是否执行初始化动作，初始值未False
    · 在__init__方法中，判断init_flag是否为False，是则初始化
    · 然后将init_flag设置为True
    · 这样就不会被再次执行
"""


class MusicPlay(object):

    instance = None

    # 定义一个类属性 init_flag，标记是否执行初始化动作，初始值未False
    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):

        # 判断init_flag是否为False，是则初始化
        if MusicPlay.init_flag:
            return

        print("播放器初始化·")

        # 然后将init_flag设置为True
        MusicPlay.init_flag = True


play1 = MusicPlay()
print(play1)

play2 = MusicPlay()
print(play2)