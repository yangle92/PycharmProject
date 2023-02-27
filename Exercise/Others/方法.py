
class Person():
    """
    这是一个类
    """
    age=18
    def shili(self):
        print("实例方法",self)

    @classmethod
    def leifangfa(cls):
        print("类方法",cls)

    @staticmethod
    def jingtai():
        print("静态方法")

#1)实例方法默认传递的第一个参数是实例本身，实例是由类实例化而来，所以他能继承类的属性。
p = Person()
print(p.age)
p.shili()
#2)类方法默认传递的一个参数是类的本身，只有类的属性
help(Person)
print(Person.__doc__)
# def Test(var,*args,**kwargs):
#     print(var,args,kwargs)
#     print(type(var),type(args),type(kwargs))
#
# Test(1)
# Test(1,2,3,A=1,B=2)

print(a)
