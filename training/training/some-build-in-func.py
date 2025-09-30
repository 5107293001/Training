# map
# filter
# enumerate
# zip
# lambda

# def add(x,y):
#     return x+y

# add = lambda x, y : x+y
# print(add(2,3))

def sq(x):
    return x**2

ls: list[int] = [1,2,3,4,5]

sls : list[int] = map(lambda x : x**2,ls)
sls : list[int] = map(sq,ls)
print(list(sls))


names : list[str] = ['Daniel laruso', 'John Kreese', 'Johny Lawrence']
dojo : list[str] = ['Miyagi-do','Cobra-kai','Cobra Kai']
ages : list[int] = [45,75]

combinded_data = zip(names,dojo,ages)
print(list(combinded_data))

names : list[str] = ['Daniel laruso', 'John Kreese', 'Johny Lawrence']

print(list(enumerate(names,start=101)))

for idx, name in enumerate(names,start=102):
    print(idx,name)

for name in enumerate(names,start=102):
    idx , name = name
    print(idx, name)

nums : list[int] = [1,2,3,4,5,6,7,8,9,10]

evens = filter(lambda x:x%2==0,nums)

print(list(evens))



