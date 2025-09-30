# In python list is like an array having multiple type of object in it

ls1 = [1,2.3,'rajan',True]
print(ls1)

emptyls = []
emptyls = list()
nestedls = [1,2,[3,4],5]
print(nestedls)
mixedls = [1,2.3,'rajan',True,[1,2,3],(1,2),{1,2}, {1:'rajan',2:'mady'}]


ls2 = [1,2,3,4,5]
print(ls2[0])
print(ls2[-1])
print(ls2[1:4])

ls2[2] = 10
ls2[1:4] = [20,30]
print(ls2)


ls3 = ['a','b','c','d','e'] 
# ls3[1] = 'r'
# ls3[4] = 'z'
# print(ls3)
ls3[1:4] = ['x','z']
print(ls3)

ls1 = [1,2,3]
ls2 = [4,5,6]
print(ls1 + ls2)
print(ls1 * 3)
print(4 in ls1)

print(len(ls1))

ls4 = [1,2,3]
ls4.append(4)
ls4.append(11)
ls4.append(10)
print(ls4)
ls4.append([5,6])
print(ls4)
ls4.extend([7,8])
print(ls4)
ls4.insert(2,2.5)
print(ls4)
ls4.remove(2.5)
print(ls4)
popped_item = ls4.pop()
print(popped_item)
print(ls4)
ls4.pop(3)
print(ls4)
ls4.append(3)
print(ls4)
ls4.remove(3)
print(ls4)
# ls4.clear()
# print(ls4)
ls4.append(3)
print(ls4)
print(ls4.index(2))
print(ls4.count(3))
ls4.reverse()
print(ls4)
ls5  = ls4.copy()
print(ls4)