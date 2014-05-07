 #-*- coding: UTF-8 -*-
# class CAnimal:
#     name = 'unnmae' #memeber name
#
#     def __init__(self1, voice='hello'):
#         self1.voice = voice
#         print "CAnimal Constructor......"
#
#     def __del__(self2):
#         pass
#         print "CAnimal Destructor......."
#
#     def Say(self3):
#         print self3.voice
#
#     def Run(self):
#         pass
#
#
# class CDog(CAnimal):
#     name = ""
#     age = 0
#     __weight = 0
#     voice = "voice"
#
#
#     def __init__(self):
#         print "CDog Constructor...."
#
#     # def __del__(self):
#     #     print "CDog Destrutor....."
#
#
#     def SetVoice(self, voice="wow"):
#         self.voice = voice
#
#
#     def Run(self):
#         print "Running"
#
#     def Print(self):
#         print "Name: %s" % (self.name)
#         print "Age:  %d" % (self.age)
#         print "Wight:%d" % (self.__weight)


# t = CAnimal()
# t.Say()
# print t.name
#

# bobo = CDog()
# bobo.SetVoice("My name is Bobo!")
# CDog.voice = "Hello world!"
# CDog.name  = "hello world"
# bobo.Say()
# bobo.Run()
# bobo.Print()


class ZZClass(object):
    classNum = 0
    def __init__(self):
        self.num = 1
        ZZClass.classNum += 1
        print ("ZZClass _init__ called.")


    def __del__(self):
        ZZClass.classNum -= 1;
        print ("ZZClass __del__ called.")


    def Hello(self):
        print("hello world!")
        self.PrintClassNum(10) #普通函数中可以调用静态函数

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    @staticmethod
    def PrintClassNum(num=100):
        print (ZZClass.classNum) #在静态方法中只能通过类名访问类变量
        #print classNum          #在静态方法中不能直接访问类变量
        #print self.num          #在静态方法中不能访问实例变量
        print num

    @classmethod
    def ClassMethod(cls):
        #print cls.num           #在类方法中不能直接访问实例变量
        print "class method."
        print cls.classNum       #在类方法中可以直接访问类变量




myObj = ZZClass()
myObj.Hello()
ZZClass.PrintClassNum(10) #可以通过类名来访问静态方法
myObj02  = ZZClass()
myObj02.PrintClassNum()   #可以通过对象实例来访问静态方法
print myObj.classNum      #可以通过对象实例来访问类变量
print ZZClass.classNum    #可以通过类名来访问静态变量


myObj.setNum(10)
myObj02.setNum(20)
print myObj.getNum()
print myObj02.getNum()

myObj02 = 0
print ZZClass.PrintClassNum()

print ZZClass.ClassMethod() #通过类调用类方法
print myObj.ClassMethod()   #通过实例调用类方法