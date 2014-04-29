o = ('a','b','c',('d1','d2'))
print(o[0])
print(o[3])
print(o[3][1])

o1 = ()
print o1

o2 = (1,)
print o2

print ;
tuple("abc")

hello = 1
print hello

hello = "hello"
print hello

import sys
sys.stdout.write('hello world!\n')
print sys.platform
print sys.version


ls1 = range(2,10,2)
print ls1 #[2, 4, 6, 8]


def foo():
    "This is a doc string."
    print "foo funtion called."
    return True

foo()