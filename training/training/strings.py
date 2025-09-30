name = 'mady'
description = '''
Hello, 
How are you?
'''
'''
This code is for training purpose 
'''

# we can also use " quotes to create a string

#String Slicing and Indexing
name="rajan" # because indexing start bwith 0 in cocding
print(name[4])
print(name[-1])

# In rajan from left to right indexing is start 0 to 4
# and also reverse indexing is start with -1 to -5 from right to left


#String Slicing
print(name[0:3]) # o/p - raj
#syntax -> str[startIndex:stop index]
print(name[:3])
print(name[2:])
print(name[:])
print(name[-3:])
print(name[-3:-1])
print(name[-3:-5]) #this otput is empty

# now talk about methods of string and function
num = 10
num2 = str(num)
print(type(num))
print(type(num2))

print()
name2='RAJA,N'
print(name.lower())
print(name2.upper())
print(name.capitalize())
desc = "   my name is Rajann      k"
print(desc)
print(desc.strip())
print(desc.rstrip())
print(desc.lstrip())
print(name2.replace('A','b'))
print(name2.split(','))
print(name2.count('A'))
name3 = 'Madan Trivedi'
print(name3.split(' '))


#Loop in string
# for n in name3:
#     print(n)
# name3[0] = 'R'
print(name3)
print(name2 + name3)
name = 'Mady'
print(name[::-1])
print(name[::-2])
# str[startIndex:stopIndex,stepIndex]