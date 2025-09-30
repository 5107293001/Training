#Tuple is immutable, ordered collections of elements
# similiar to lists they can not be changed means we can not add, remove and modify after tuple is created

t1 = ()
print(t1)
t2 = tuple()
print(t2)

t3 :tuple[int] = (1,2,3)
print(t3)

t5 = (4)
print(t5) # this is inetger

t4 = (4,)
print(t4)

fet :int = t3[0]
print(fet)

 # all slicing and indexing can be performed in tuple but not modifying elemnet by accessing it using indexing

t6 = (3,4,5)
print(t3+t6)
print(t3*3)

t7 :tuple[int] = (1,2,3,4,5,6,7,2)
print(t7[::-1])
print(t7[1:4])

print(t7.count(2))
print(t7.index(2))
print(t7.index(4))

a, b, c, d, e = (1,2,3,4,5)
print(a)
print(b)
print(c)
print(d)
print(e)

a, b, c = 1,2,3
print(a,b, c)







