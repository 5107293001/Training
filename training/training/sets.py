#SETS

# Sets is built in data type used to store unordered unique elements
# they are like mathematical sets


# Unorder  - no indexing and no slicing


s1 : set[int] = {1,2,3}
print(s1)

s2 : set[int] = set([1,2,3, 3])
print(s2)

s3: set[int] = set()
print(s3)

# n: set[int] = s2[1:2]
# print(n)

s4 : set[int] = {1,2,3,4,5}
print(s4)
s4.add(6)
print(s4)
s4.remove(2)
print(s4)
# s4.remove(2)
# print(s4)
s4.discard(2)
print(s4)
s4.discard(3)
print(s4)
s4.discard(7)
print(s4)
s4.pop()
print(s4)
s4.pop()
print(s4)
s4.clear()
print(s4)

# s5 : set[int] = {2,3,4}
# s6 : set[int] = {4,5,6}
# print(s5 + s6)

s5 : set[int] = {2,3,4}
s6 : set[int] = {4,5,6}
print(s5.union(s6))
print(s5 | s6) # '|' is union operand

print(s5.intersection(s6))
print(s5 & s6) # '&' is intersection operand


print(s5.difference(s6))
print(s6.difference(s5))
print(s5 - s6) # '-' is differfence operand

# s5.update(s6)
# print(s5)

print(s5.symmetric_difference(s6))
print(s5 ^ s6)

print(s5.issubset(s6))

s7 : set[int] = {2,3}
print(s7.issubset(s5))
print(s5.issubset(s7))


print(s7.issuperset(s5))
print(s5.issuperset(s7))

print(s5.isdisjoint(s7))
print(s7.isdisjoint(s5))

s8: set[int] = { 8,9 }
print(s8.isdisjoint(s5))
print(s5.isdisjoint(s8))










