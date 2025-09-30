# Looping on dictionary

dict1 = {
   'name' : 'John',
   'surname' : 'Kreese',
   'profession' : 'Sensei',
   'buisness' : 'Cobra Kai karante',
   'age' : 70
}

print(dict1['name'])

for d in dict1:
    print(d)

for d in dict1:
    print(dict1[d])


print(dict1.keys())

for key in dict1.keys():
    print(key)

print(dict1.values())

for value in dict1.values():
    print(value)


# a, b = [1,2]
a, b = (1,2)

print(a)
print(b)

print(dict1.items())

for key, value in dict1.items():
    print(key, value)


for surname in dict1:
    print(surname)