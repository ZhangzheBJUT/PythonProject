#import  sys
list = [1,2,3,4]
try:
    print(list[3])
except:
    print("error")
else:
    print("no error")
finally:
    print("finally")



try:
    print(list[5])
except:
    print("error")
else:
    print("no error")
finally:
    print("finally")


try:
    list[2]/0
except IndexError:
    print("indexError")
except ZeroDivisionError:
    print("zeroDivisionError")
else:
    print "no error"
finally:
    print("finally")



#define custom exception
class LengthRequiredException(Exception):
    def __init__(self,length,minLength):
        Exception.__init__(self)
        self.length = length
        self.minLength=minLength

l = [1,2,3,4,5,6]
minLength = 6

try:
    raise LengthRequiredException(len(l),minLength)
except IndexError:
    print("index out of bounds")
except LengthRequiredException:
    print("Length Error.")
    #print("Length not fit:length is %d required %d" %(LengthRequiredException.length,LengthRequiredException.minLength))
else:
    print("no exception was raised.")
finally:
    print("finally will be execute")



class Test(object):
    def __enter__(self):
        print ("enter....")
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit.....")
        return True

#with Test() as t:





#var = Test()


#!encoding:utf-8
class echo :
    def output(self) :
        print 'hello world'
    def __enter__(self):
        print 'enter'
        return self #返回自身实例，当然也可以返回任何希望返回的东西
    def __exit__(self, exception_type, exception_value, exception_traceback):
        #若发生异常，会在这里捕捉到，可以进行异常处理
        print 'exit'
        #如果改__exit__可以处理改异常则通过返回True告知该异常不必传播，否则返回False
        if exception_type == ValueError :
            return True
        else:
            return False
#
# with echo() as e:
#     e.output()
#     print 'do something inside'
# print '-----------'
# with echo() as e:
#     raise ValueError('value error')
# print '-----------'
# with echo() as e:
#     raise Exception('can not detect')
#
#
#





