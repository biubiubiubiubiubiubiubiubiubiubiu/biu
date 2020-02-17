#x = 'aaa'.split('aaa')
#print (x)

import copy

person=['name',['a',100]]

p1=copy.copy(person)
p2=person[:]

p1[0]='alex'
p2[0]='fengjie'

p1[1][1]=20

print(p1)
print(p2)

