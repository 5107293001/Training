# Comprehension works only on connections


#list comprehension

num_ls = [1,2,3,4,5,6]
sq_ls = []
for num in num_ls:
    sq_ls.append(num**2)
print(sq_ls)


sq_ls = [num**2 for num in num_ls]
print(sq_ls)

even_sq_ls = [num**2 for num in num_ls if num % 2 == 0]
print(even_sq_ls)



#dict comprehnsion
details = {
    'john123':{
        'name':'John Kreese',
    },
    'laruso1234':{
        'name':'Daniel Laruso'
    },
        'johny345':{
        'name':'Johny'
    }
}

new_details = { d:details[d] for d in details if details[d]['name'] != 'Johny'}
print(new_details)

{'john123': {'name': 'John Kreese'}, 'laruso1234': {'name': 'Daniel Laruso'}}


# Mereg Things

num_ls = [1,2,3]
num_ls2 = [4,5,6]
print([*num_ls,*num_ls2])

# dict merge 
d1 = {
    'a':1,
    'b':2
}
d2 = {
    'c':3,
    'd':5
}
print({**d1,**d2})


