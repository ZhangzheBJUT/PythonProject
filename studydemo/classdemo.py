class CAnimal:
    name = 'unnmae' #memeber name

    def __init__(self1,voice='hello'):
        self1.voice = voice
        print "CAnimal Constructor......"

    def __del__(self2):
        pass
        print "CAnimal Destructor......."

    def Say(self3):
        print self3.voice

    def Run(self):
        pass

class CDog(CAnimal):
    name = ""
    age  = 0
    __weight = 0
    voice = "voice"


    def __init__(self):
        print "CDog Constructor...."

    # def __del__(self):
    #     print "CDog Destrutor....."


    def SetVoice(self,voice="wow"):
        self.voice = voice


    def Run(self):
        print "Running"

    def Print(self):
        print "Name: %s"  %(self.name)
        print "Age:  %d"  %(self.age)
        print "Wight:%d"  %(self.__weight)






# t = CAnimal()
# t.Say()
# print t.name
#

bobo = CDog()
bobo.SetVoice("My name is Bobo!")
CDog.voice = "Hello world!"
CDog.name  = "hello world"
bobo.Say()
bobo.Run()
bobo.Print()

