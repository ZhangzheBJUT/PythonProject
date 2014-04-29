# def myfunc():
#     print("myfunc() called.")
#
# myfunc()
# myfunc()



# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("after myfunc() called.")
#     return func
# def myfunc():
#     print("myfunc() called.")
# myfunc = deco(myfunc)




# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("after myfunc() called.")
#     return func
#
# #myfunc = deco(myfunc)
# @deco
# def myfunc01():
#     print("myfunc() called.")
#
# myfunc01()
# myfunc01()


# def deco(func):
#     def _deco():
#         print("before myfunc() called.")
#         func()
#         print("  after myfunc() called.")
#     return _deco
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#     return 'ok'
#
# myfunc()
# myfunc()


# def deco(func):
#     def _deco(a,b):
#         print ("before myfunc() called.")
#         ret = func(a,b)
#         print("after myfunc() called.result:%s" %ret)
#         return ret
#     return _deco
#
# @deco
# def myfunc(a,b):
#     print("myfunc(%s,%s) called." %(a,b))
#     return  a+b
#
# myfunc(1,2)
# myfunc(3,4)



# def deco(func):
#     def _deco(*args, **kwargs):
#         print("before %s called." % func.__name__)
#         ret = func(*args, **kwargs)
#         print("  after %s called. result: %s" % (func.__name__, ret))
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a+b
#
# @deco
# def myfunc2(a, b, c):
#     print(" myfunc2(%s,%s,%s) called." % (a, b, c))
#     return a+b+c
#
# myfunc(1, 2)
# myfunc(3, 4)
# myfunc2(1, 2, 3)
# myfunc2(3, 4, 5)


def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print(" myfunc() called.")

@deco("module2")
def myfunc2():
    print(" myfunc2() called.")


myfunc()
myfunc2()



