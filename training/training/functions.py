# functions


# a = int(input('Please enter first number :'))
# b = int(input('Please enter second number : '))

# print(a+b)

# print(b-a)
# print(b*a)

def calculator():
    print('This is basic function')


calculator()
calculator()


def name(fname : str):
    print(fname)

name('John')

def decr(fname :str , lname:str):
    print(fname, lname)

decr('John','Kreese')
# decr('John')

def mul(num : int , multiplier :int = 1):
    print(num * multiplier)

# def mul(multiplier :int = 1,num : int):
#     print(num * multiplier)


mul(2)
mul(2,4)

n = name('Daniel laruso')
print(n)

def div(num:int,divident:int=1) -> float:
    return num/divident

# def div(num:int,divident:int=1) -> float:
#     d = num/divident
#     return d

op = div(10)
print(op)


def doctor():
    pass



