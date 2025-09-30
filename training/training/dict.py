# Dictionary 
# - Unordered
# - Mutable
# - Key - valur pair

desc : dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(desc)

desc2 = dict(name="Rajan", age=25, city="Delhi")  # Create by built in function in which pass the arguments with values
print(desc2)


emp1 = {}
emp2 = dict()
print(emp1, emp2)

name = desc["name"]
age = desc.get('age')
print(name)
print(age)
# surname = desc['surname']
# surname = desc.get('surname')  # None
surname = desc.get('surname','kreese')  # None
print(surname)


desc['age'] = 40
desc['email'] = 'john.kreese@gmail.com'
print(desc)

del desc['city']
print(desc)
# email = desc.pop('email')
# print(email)
print(desc.pop('email'))
print(desc)


desc4 = {
    "name": "Mady",
    "age": 28,
    "city": "Mumbai",
    "skills": ['python','ML','AI'],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}
print(desc4)

print(list(desc4.keys()))
print(list(desc4.values()))
print(list(desc4.items()))

desc5 = {
    "phone": "123-456-7890",
    "email": "mt@gmail.com"
}
desc4.update(desc5)
print(desc4)

dup_desc4 = desc4.copy()
dup_desc4['name'] = 'Rajan'
# desc4['name'] = 'Madhur TIwaree'
print(dup_desc4)
print(desc4)

desc4.clear()
print(desc4)

desc6 = {
    'name': "Rajan",
    'age': 25,
    'city': "Delhi",
    "address":{
        "street": "456 Another St",
        "zip": {
            "code": "110001",
            "plus4": "1234"
        }
    }
}


print(desc6['address']['zip']['code'])
desc6['address']['zip']['code'] = '999999'
print(desc6)


d1 : dict = {'a': 1, 'b': 2}

s1 : str = str(1)
print(d1)






