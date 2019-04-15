#Concatenating Lists Using +
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print(a)

print('\n')

#List can be sliced using :
t=[9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print('\n')

#Building a List from Scratch
stuff = list()
stuff.append('book')
stuff.append(9)
print(stuff)
stuff.append('Apple')
print(stuff)

print('\n')

#Is Something in a List ?

some = [1,9,21,10,16]
print(9 in some)
print(15 in some)
print(20 not in some)


print('\n')

#Sorting List
friends = ['Nitin','Rahul','Aman']
friends.sort()
print(friends)
print(friends[0])
