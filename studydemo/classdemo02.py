 #-*- coding: UTF-8 -*-

__author__ = 'yinrunmin'

class MethodTest():
    var1 = "class var"

    def __init__(self,var="object var"):
        self.var2 = var;

    @staticmethod
    def staticFunc():
        #print var2 #error cannot access instance member.
        print "static method."

    @classmethod
    def classFunc(cls):
        #print var2 #error cannot access instance member.
        print cls.var1
        #print cls.var2 #class MethodTest has no attribute 'var2'
        print "class method."



#1.都可以通过类或实例调用
mt = MethodTest()
mt.staticFunc()
mt.classFunc()
MethodTest.staticFunc()
MethodTest.classFunc()

#2.都无法访问实例成员



#3.staticmethod和classmethod的区别:
'''1.staticmethod无需参数，classmethod需要类变量作为参数传递（不是类的实例）
    def classFun(cls):
        print 'class method'  //cls作为类变量传递
2.classmethod可以访问类成员，staticmethod则不可以
    @staticmethod
    def staticFun():
        print var1  //wrong
    @classmethod
    def classFun(cls):
        print cls.var1  //right'''



#类变量和实例变量的区别：http://blog.csdn.net/gukesdo/article/details/7453227
class classA:
    classVar = ''
    def __init__(self):
        pass

    def set_var1(self,x):
        classA.classVar= x

    def set_var2(self,y):
        self.var2 = y
        return self.var2


oa = classA()
ob = classA()

oa.set_var1("class variable.")
print oa.classVar #class variable.
print ob.classVar #class variable.

oa.classVar = "changed."
print oa.classVar  #changed.
print ob.classVar  #class variable.

oa.set_var1("class variable01")
print oa.classVar #changed.
print ob.classVar #class variable01


ob.set_var1("class variable02")
print oa.classVar  #changed.
print ob.classVar  #class variable02

ob.set_var2("inst variable")
print ob.var2
#print oa.var2  #error! because var2 is a instance variable



class Test:
    count =  0
    def __init__(self,c):
        self.count = c
        self.__name="zhangzhe" #私有变量
        self.__class__.count = self.__class__.count +1

    def __get_name(self): #私有方法
        return self.__name

    def get_counte(self):
        return self.count

a = Test(3)
print a.count #3
#print a.name  #AttributeError:Test instance has no attribute 'name'
print Test.count #1
print a.get_counte()
#print a._Test_name

print a.__dict__  #{'count': 3, '_Test__name': 'zhangzhe'}
print a._Test__name


b = Test(-1)
print b.count    #1
print Test.count #2


