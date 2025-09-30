# In python we have basic or built in data types or Collection data types

#Basics data types are

#Integer
num1 = 5  # int num1;
print(num1)

#float
float1 = 54.6  # float num1;
print(float1)

#complex number
complex = 2+3j #Real Number + imaginary
print(complex)

#Bool 
bool1 = True;
bool2 = False;
print(bool1, bool2, sep='\n')


#string 
# A string is collection of characters or words in quotes, Quotes may be single orn double
# But in python we do not allow the single quote in single quote and double quote in double quote
# But we allow to single quote in double or vice versa
# if we want to use single in single quote and double in double quote then we should use the escape sequences
# Documnet string or multiline string using three single or double quotes
 
str1 = 'Anuj'
str2 = "You are tutor"
# str3 = 'Anuj 'Anuj' 
# str4 = "Anuj "Anuj "
str5 = 'Anuj "Trivedi" '
str6 = "Anuj 'Trivedi "
str7 = 'Anuj \'Trivedi\' '
str8 = "Anuj \"Trivedi\" "
str9 = '''
    I am tutor,
    I am tutor
'''

"""
This code is for data types.
"""
print(str1,str2, sep='\n')
print(str7)
print(str8)
print(str9)


# Collection data types
#1. List
#2. tuple
#3. set
#4. dict

# Collection and any data types items in square bracket , called the list or array
# list ordered, mutable
ls1 = [1,2,'anuj', {'name':'anuj'},{2,3}, (3,6)] 
ls2 = []
ls3 = list()

# tuple
# Ordered, immutable
t1 = tuple()
t2 = ()
t3 = (1,"anuj")
print(t1,t2, t3)


# Set 
#unordered or allow unique item
s1 = {}
s2 = set()
s3 = {1,2,3}
s4 = {1,3,2, "anuj"}
print(s4)


#Dict

