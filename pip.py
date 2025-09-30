import camelcase
import random
c= camelcase.CamelCase()
text="This texts in small case"
print(c.hump(text))

x: int =5
print(type(x))

print("===============type conversion")
a : int = 10
print(float(a))

b: float= 20.25
print(int(b))

print('===============Random')
print(random.randrange(1,5))


print('===============String')
count: str = ("This is our Python Class")
print(len(count))
print(count[0])
print(count[5])



for x in  (count):
    print(x)


print("our" in count ) 
print("Python" not in count ) 
print("abc" not in count )


print(count [3:7])
print(count[: 10])
print(count[3:])
print(count.upper())
print(count.lower())
print(count.replace("our","x"))


print(count[: :])


text: str = ("   This is our Python Class")
print(text.strip())
text1: str = ("This is, our Py,thon Class")
print(text1.split(",")) 

print("COncatination=====", text+text1)


name :str = "Rajan"
age: int= 8
print("string formatting===============")
print(f"my name is {name }, and I am {age}")


print("list======================")
fruits : list = ["Banana", "Apple", "Mango", "Cherry"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[2 : ])
print(fruits[:])
print(fruits[-2 : -1])
print(fruits[0: 2])

fruits [0]= "Orange"
print(fruits)
# To do check from Sweta
fruits[2:3]= ["Watelmelon", "Grapes", "Tomato"]
print(fruits)

a,b,c= 1,2,3\





# while n in range(1,n):
#     print(n)
#     n =+ 1




