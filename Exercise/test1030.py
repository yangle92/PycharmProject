#############################高阶函数：当一个函数A的参数，接收的又是另一个函数，则把这个函数A称为是高阶函数
# l = [
#     {"name":"Mike","age":18},
#     {"name":"Tony","age":19},
#     {"name":"Eric","age":22},
# ]
#
# def getKey(x):
#     return (x["name"])
#
# re = sorted(l,key=getKey)
# print(re)
#高阶函数运用场景
# def caculate(num1,num2,caculateFunc):
#     print(caculateFunc(num1,num2))
#
# def sum (a,b):
#     return a+b
# def jianfa(a,b):
#     return a-b
#
# caculate(1,2,sum)
# caculate(3,4,jianfa)
################################返回函数：一个函数内部，它返回的数据是另外一个函数，把这样的函数称为返回函数

# def getFun(falg):
#     def sum(a,b,c):
#         return a+b+c
#     def jian(a,b,c):
#         return a-b-c
#     if falg == "-":
#         return jian
#     elif falg == "+":
#         return sum
# result = getFun("+")
# print(result,type(result))
# re=result(1,2,3)
# print(re)

#####匿名函数 就是没有名字的函数 lambda

# res=(lambda x,y:x+y)(1,2)
# print(res)

# l = [
#     {"name":"Mike","age":18},
#     {"name":"Tony","age":19},
#     {"name":"Eric","age":22},
# ]
# #
# # def getKey(x):
# #     return (x["name"])
# #
# re = sorted(l,key=lambda x:x["name"])
# print(re)


######################闭包
#在函数嵌套的前提下
#内层函数引用了外层函数的变量，包括参考
#外层函数，又把内层函数当做返回值进行返回
# def test():
#     a=10
#     def test2():
#         print(a)
#     return test2
#
# newFunc = test()
# newFunc()
#应用场景：外层函数，根据不同的参数，来生成不同作用功能的函数

# def line_config(content, length):
#     def line():
#         print("#"*(length//2)+content+"#"*(length//2))
#     return line
#
# line1 = line_config("hello",20)
# line1()
# line1()
# line1()
# line2 = line_config("world",20)
# line2()


