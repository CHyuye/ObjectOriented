# 1、文件基本操作
"""
    三个步骤： 一个函数open，三个方法
    1、open —— 打开文件，并且返回文件操作对象
    2、读，写文件
        read —— 将文件内容读取到内存
        write —— 将指定内容写入文件
    3、关闭文件 close
"""

# 打开文件，默认是只读模式
# file = open("README")
#
# # 读取文件
# # 读取完文件后，文件指针会移动到文件末尾
# text = file.read()
# print(text)
# print(len(text))
#
# print("-" * 30)
#
# # 当执行了一次read方法，读取了内容，再次调用read方法，不能获取到内容
# text = file.read()
# print(text)
# print(len(text))
#
# # 关闭文件
# # 不要忘记关闭文件，会造成系统资源浪费，而且会影响到后续文件访问
# file.close()


# 2、文件指针（知道）
"""
    文件指针标记从哪个位置开始读取数据
    第一次打开文件，通常文件指针在开始位置
    当执行read方法后，文件指针移动到末尾
"""

# 3、打开文件的方式
"""
    访问方式：
    r —— 只读方式打开文件，默认模式
    w —— 只写方式打开文件，如果文件存在，文件内容会被重写覆盖，文件不存在创建文件
    a —— 追加方式打开文件，文件存在，文件指针放在文件末尾，写入，文件不存在创建文件
    
    不常用的三种：频繁的移动文件指针，会影响文件的读写效率
    r+ —— 以读写方式打开，文件指针放在开头
    w+ —— 以读写方式打开，文件存在，文件内容覆盖，不存在，创建文件
    a+ —— 以读写方式代开，文件存在，文件指针在末尾，写入，文件不存在创建文件
"""

# open语法： file = open("文件名", "访问方式")
# file = open("README", "a")
#
# file.write("\nI love you")
#
# file.close()


# 4、使用readline 分行读取大文件
# file = open("README")
#
# while True:
#     # 读取每一行内容
#     text = file.readline()
#
#     # 判断是否读到内容
#     if not text:
#         break
#
#     # 每读取一行的末尾都已经加上了 '\n'
#     print(text, end="")
#
# file.close()


# 5、复制小文件
# 打开源文件，创建新文件
# read_file = open("README")
# write_file = open("README[复件]", "w")
#
# # 读取源文件，写入新文件
# text = read_file.read()
# write_file.write(text)
#
# # 关闭文件
# read_file.close()
# write_file.close()


# 6、复制大文件
# 打开源文件，创建新文件
# read_file = open("README")
# write_file = open("README[复件]", "w")
#
# # 使用readline 分行读取大文件，减轻内存消耗资源
# while True:
#     # 读取每一行内容
#     text = read_file.readline()
#
#     # 判断是否读到内容
#     if not text:
#         break
#
#     write_file.write(text)
#
# # 关闭文件
# read_file.close()
# write_file.close()
