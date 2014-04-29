class ObjectCreator(object):
    """ObjectCreator doc....."""
    pass

print ObjectCreator.__doc__


my_object = ObjectCreator()
print my_object

print ObjectCreator

def echo(o):
    print o

echo(ObjectCreator)
print hasattr(ObjectCreator,'new_attribute')
ObjectCreator.new_attribute = 'foo'
print hasattr(ObjectCreator,'new_attribute')


obj1 = ObjectCreator()
obj2 = ObjectCreator()

print obj1.new_attribute

obj1.new_attribute = 'obja'
obj2.new_attribute = 'objb'

print obj1.new_attribute
print obj2.new_attribute


ObjectCreatorMirror = ObjectCreator
print  ObjectCreatorMirror()


def choose_class(name):
    if name == 'foo':
        class foo(object):
            pass
        return foo
    else:
        class Bar(object):
            pass
        return  Bar

Myclass = choose_class('Bar')
print  Myclass


print type(1)
print type("1")
print type(ObjectCreator)
print type(ObjectCreator())


class classA:
    var1=0
    def __init__(self,text):
         self.var2=text    #var2 is a instance variable
                           ##       self.var1=init_value #it will make var1 as a instance variable
    def show(self):
        print self.var1, self.var2
    def set_var1(self, x):
        self.var1=x


print hasattr(classA,'var1')
print hasattr(classA,'var2')
oa=classA('a')
ob=classA('b')
print '---init---'
oa.show()
ob.show()
print classA.var1, 'classA'


classA.var1=1
print '---after classA.var1=1---'
oa.show()
ob.show()
print classA.var1, 'classA'

oa.var1=2
oa.var3=4
print '---after oa.var1=2---'
oc=classA('c')
oa.show()
print oa.var3
ob.show()
oc.show()
print classA.var1, 'classA'



oa.set_var1(3)
ob.set_var1(4)
print '---after oa.set_var1(3),ob.set_var1(4)---'
oa.show()
ob.show()
oc.show()
print classA.var1, 'classA'
print hasattr(classA,'var1')

classA.var1=10
print '---after classA.var1=5---'
oc=classA('c')
oa.show()
ob.show()
oc.show()
print classA.var1, 'classA'


print type(1)
print type("1")
print type(int)
print type(ObjectCreator)
print type(ObjectCreator())


MyShinyClass = type('MyShinyClass',(),{})
print MyShinyClass
print MyShinyClass()

Foo = type('Foo',(),{'bar':True})
print Foo
print Foo.bar
f = Foo()
print f
print hasattr(Foo,'bar')


FooChild = type('FooChild',(Foo,),{})
print FooChild
print FooChild.bar

def echo_bar(self):
    print self.bar
FooChild01 = type('FooChild01',(Foo,),{'echo_bar':echo_bar})
print hasattr(Foo,'echo_bar')
print hasattr(FooChild01,'echo_bar')

my_foo = FooChild01
my_foo()


def upper_attr(fuc_class_name,future_class_parents,future_class_attr):
    attrs = ((name,value) for name,value in future_class_attr.itmes if not name)
    uppercase_attr = dict((name.upper(),value) for name,value in attrs)
    return type(fuc_class_name,future_class_parents,uppercase_attr)

#__metaclass__ = upper_attr

class Foo(object):
    __metaclass__ = upper_attr
    bar = 'bip'

print "######"
print hasattr(Foo,'bar')
print hasattr(Foo,"BAR")