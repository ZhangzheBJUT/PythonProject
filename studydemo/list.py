
list = [1,2,3,4,5]
length = len(list)
print length
print list

list.append("hello world")
print list

list.remove(2)
print list

list2 = [7,8,9]
list3 = list + list2
print  list3


list4 = [123,'abc',['def','list'],(7-9j,2+3j)]
print list4[2][1]
print list4[3][1]


list.extend(list2)
print list

arr = ('a','b','c')
list.append(arr)
print list

list.reverse()
print list

list.append(0)
list.sort()
print list


index = list.index(5)
print index


list.pop(0)
print list


list.append(1)
list.append(1)
list.append(1)
c=list.count(1)
print list
print c


list.remove(('a','b','c'))
print list

list.pop(1)
print list





ls1 = ['abc',123]
ls2 = ['xyz','789']
ls3 = ['abc',123]
print ls1 <ls2
print ls2 < ls3
print (ls2>ls3 and ls1==ls3)
print ls1[-2]
ls1[0] = ls2
print ls1




mixup_list = [4.0,[1,'x'],'beef',(-1.9+6j)]
print 'beef' in mixup_list #True
print 'x'in mixup_list #False
print  'x' in mixup_list[1] #True


print mixup_list + ls1


ls1 = ['1','2']
ls2 = ls1 * 2
ls1 *= 2
print ls2
print ls1



ls1 = [8,-2,5]
ls2 = [i*2 for i in ls1]
print ls2


ls1 = range(30)
print ls1


initial_value = 2
list_length = 5
sample_list = [ initial_value for i in range(10)]
print sample_list
sample_list = [initial_value]*list_length

for element in sample_list:
    print element
#
# example = [0,1,2,3,4,5,6,7,8,9]
# print (example[4:8])
# print (example[:8])
# print (example[:])
# print (example[1:8:2])


#
# ex=[1,2,3,4,5,6]
# ex[4:] = [9,8,7]
# print (ex)
#
# ex[1:1]=[0,0,0]
# print (ex)
#
# del ex[0:2]
# print (ex)

#
# one = [1,2,3]
# two = [1,2,3]
# print(one == two)
# print(one is two)
#
# del list
#
# str = "abcdefg"
# print(str[0])
# print (list(str))
#
# s = "abcdefg"
# print('a' in s)
#
#
# import math
#
# se = math.sqrt
# print(se(81))

