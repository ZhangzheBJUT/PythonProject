class people:
    #define attribute
    name = ''
    age  = 0
    #define private attribute
    __weight = 0
    def __init__(self,n="hello",a=24,w=45.9):
        self.name = n
        self.age  = a
        self.__weight = w
    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name,self.age))
    def weight(self):
        print("Weight number:%d" % (self.__weight))
    def __del__(self):
        print("people desconstructor........")
    def __repr__(self):
        print("I am a people class instance")


p = people('tom',10,30)
p.speak()
print p.name
print p.age
p.weight()

p2 = people()
p2.speak()
#print p.__weight

# people.name = 'zhangzhe'
# print p.name
# print p2.name

#print p2

#print p
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g


    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d" % (self.name,self.age,self.grade))

    def __del__(self):
        print("student desconstructor......")

# s  = student('ken',20,60,3)
# s.speak()


class speaker():
    topic = ''
    name  = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("I am %s,I am a speaker!My topic is %s " % (self.name,self.topic))
    def __del__(self):
        print("speaker desconstructor.....")

class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)


    def __del__(self):
        print ('sample desconstructor')
        speaker.__del__()
        student.__del__()

test = sample("Tim",25,80,4,"Python")
test.speak()















