#reference:   http://blog.csdn.net/wklken/article/details/6313265
class People:
    "People class doc."
    #attribute
    name = ''
    age  = 0
    __weight = 0

    #method
    def __init__(self,aName,aAge,aWeight):
        self.name = aName
        self.age = aAge
        self.__weight = aWeight

    def speak(self):
        print("%s is speaking:I am %d years old." %(self.name,self.age))



class Student(People):
    #attribute
    grade = 10

    #method
    def __init__(self,aName,aAge,aWeight,aGrade):
        People.__init__(self,aName,aAge,aWeight)
        self.grade = aGrade

    def speak(self):
        print("%s is speaking:I am %d years old. I am  in grade %d." %(self.name,self.age,self.grade))



class Speaker():
    topic = ' '
    name  = ' '

    def __init__(self,aTopic,aName):
        self.name = aName
        self.topic = aTopic

    def speak(self):
        print("I m %s,I am a speaker!My topic is %s." %(self.name,self.topic))


class Sample(Speaker,Student):

    a  = ''
    def __init__(self,aTopic,aName,aAge,aWeight,aGrade):
        Speaker.__init__(self,aTopic,aName)
        Student.__init__(self,aName,aAge,aWeight,aGrade)


if __name__ == "__main__":
      print "main is working."
if __name__ == "PersonClass":
    print "###########PersonClass is working."

test = Sample("Tim","my Topic",25,80,2)
test.speak()


a = 'hello'
b = 'world'



