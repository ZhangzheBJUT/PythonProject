import pickle
import struct

d = {'a':1,'b':2}
f = open('datafile.txt','wb')
pickle.dump(d,f)
f.close()


f = open('datafile.txt','rb')
e = pickle.load(f)
print e



f = open('data.bin','wb')
data = struct.pack('hhl',1,2,3)
f.write(data)
f.close()


f = open('data.bin','rb')
data = f.read()
values = struct.unpack('hhl',data)
print values



