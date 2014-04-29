#help(dict)

# class dict(object)
#  |  dict() -> new empty dictionary.
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs.
#  |  dict(seq) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in seq:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __cmp__(...)
#  |      x.__cmp__(y) <==> cmp(x,y)
#  |
#  |  __contains__(...)
#  |      D.__contains__(k) -> True if D has a key k, else False
#  |
#  |  __delitem__(...)
#  |      x.__delitem__(y) <==> del x[y]
#  |
#  |  __eq__(...)
#  |      x.__eq__(y) <==> x==y
#  |
#  |  __ge__(...)
#  |      x.__ge__(y) <==> x>=y
#  |
#  |  __getattribute__(...)
#  |      x.__getattribute__('name') <==> x.name
#  |
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |
#  |  __gt__(...)
#  |      x.__gt__(y) <==> x>y
#  |
#  |  __hash__(...)
#  |      x.__hash__() <==> hash(x)
#  |
#  |  __init__(...)
#  |      x.__init__(...) initializes x; see x.__class__.__doc__ for signature
#  |
#  |  __iter__(...)
#  |      x.__iter__() <==> iter(x)
#  |
#  |  __le__(...)
#  |      x.__le__(y) <==> x<=y
#  |
#  |  __len__(...)
#  |      x.__len__() <==> len(x)
#  |
#  |  __lt__(...)
#  |      x.__lt__(y) <==> x<y
#  |
#  |  __ne__(...)
#  |      x.__ne__(y) <==> x!=y
#  |
#  |  __repr__(...)
#  |      x.__repr__() <==> repr(x)
#  |
#  |  __setitem__(...)
#  |      x.__setitem__(i, y) <==> x[i]=y
#  |
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |
#  |  get(...)
#  |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
#  |
#  |  has_key(...)
#  |      D.has_key(k) -> True if D has a key k, else False
#  |
#  |  items(...)
#  |      D.items() -> list of D's (key, value) pairs, as 2-tuples
#  |
#  |  iteritems(...)
#  |      D.iteritems() -> an iterator over the (key, value) items of D
#  |
#  |  iterkeys(...)
#  |      D.iterkeys() -> an iterator over the keys of D
#  |
#  |  itervalues(...)
#  |      D.itervalues() -> an iterator over the values of D
#  |
#  |  keys(...)
#  |      D.keys() -> list of D's keys
#  |
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value
#  |      If key is not found, d is returned if given, otherwise KeyError is raised
#  |
#  |  popitem(...)
#  |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
#  |      2-tuple; but raise KeyError if D is empty
#  |
#  |  setdefault(...)
#  |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
#  |
#  |  update(...)
#  |      D.update(E, **F) -> None.  Update D from E and F: for k in E: D[k] = E[k]
#  |      (if E has keys else: for (k, v) in E: D[k] = v) then: for k in F: D[k] = F[k]
#  |
#  |  values(...)
#  |      D.values() -> list of D's values
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  __new__ = <built-in method __new__ of type object at 0xf9a48>
#  |      T.__new__(S, ...) -> a new object with type S, a subtype of T
#  |
#  |  fromkeys = <built-in method fromkeys of type object at 0xf9a48>
#  |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
#  |      v defaults to None.

m = {'a':1,'b':2,'c':3}
# print (m)
# print(m['a'])
# print(m.get('b'))
#
# m2= m.copy()
# print (m2)
# m2['a']=100
# print (m2)
# print (m)
#
#
# print (m.keys())
# print (m.values())
# print (m.items())
#
# m.pop('a')
# print (m)

#D.items() -> list of D's (key, value) pairs, as 2-tuples
print (m.items()) #[('a', 1), ('c', 3), ('b', 2)]

#需要注意的是：*args要放在**kwargs前面，不然会报错：
def demo(*agrs,**kwagrs):
    print 'len of agrs:',len(agrs)
    print 'agrs   = ',agrs

    print 'len of kwagrs:',len(kwagrs)
    print 'kwagrs = ',kwagrs

demo(2,3,4,5,6,7,65,a=1,b=2)


def demo02(**kwagrs):
    # print 'len of agrs:',len(agrs)
    # print 'agrs   = ',agrs

    print 'len of kwagrs:',len(kwagrs)
    print 'kwagrs = ',kwagrs

demo02(a=1,b=2)

#http://www.cnblogs.com/tqsummer/archive/2011/01/25/1944416.html

# *args 是把所有的参数按顺序打包成一个list()
# **kwargs 是把所有参数和名字打包成 dict,key 和参数名字, 值就是变量的值.
#
# 简单的说, 这里的 * 就是把参数打包或者分解出来
#
# *args 表示是一个全部参数的列表
# 此外,也可以直接用于调用
# 例如：
# def fun(a,b,c):
#     pass
#
# l=[5,7,9]
# fun(*l)
# 这个代码是可以执行的.
#
# **kwargs 是把参数打包成 dict,dict的内容就是名字和参数一一对应的。
# 但是注意，如果参数表根本没有定义参数的名字的话，这个会是个空的。
# 也就是说如果一个函数的参数本来就是
# def fun(*args, **kwargs)
# 的话,
# 如果你在调用时没有使用名字指定参数名的话, kwargs 只能得到一个空的dict()
# 具体的使用大概是在装饰函数上见得比较多.
#
# 另外， args 和 kwargs 只是推荐名字，其实你可以使用任意的变量名的。



#http://www.linuxzen.com/python-you-ya-de-cao-zuo-zi-dian.html  字典的操纵












