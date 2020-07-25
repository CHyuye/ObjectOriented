# eval函数的基本使用
# eval() 函数十分强大 —— 能将字符串当成有效的表达式来求值并返回计算值

# 案例 —— 计算器

# 因为eval() 函数很强大，所以在开发时，不能使用eval 直接转换input的结果
input_str = input("请输入您要计算的值：")

print(eval(input_str))