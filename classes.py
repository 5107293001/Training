
# Maruti Suzuki
# Making cars
# Collections Cars , different technologies, ant other things


class Any:
    pass

class Suzuki:

    desc : str = "I am a class varibale"

    def __init__(self, idesc='') -> None:
        self.idesc : str = idesc
        print("Initiated")

    def methods(self):
        print('I am suzuki')
        print(self.idesc)
        print(self.desc)

    def methos2():
        print('m2')

# obj1 = Suzuki('baleno')
# obj2 = Suzuki()
# # obj1 = {
# #     'idesc':'',
# #     'desc':'',
# #     'methods':
# # }
# print(obj1.idesc,obj1.desc)

class Calculator:

    desc : str = 'Calculator : ->'

    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1- self.num2)
    
    def mul(self):
        print(self.num1 * self.num2)


op = Calculator(23, 24)
print(op.num1)
print(op.num2)
op.add()
op.sub()
op.mul()



# __init__  this is constructor
# self Refers to the current instance of the class
# Attributes - variable that belong to an object
# Methods Function that belongs to the class
# Inheritance - Allows a class to inherit methods and attributes  from another class
# Encapsulation - Bundling data and methods that work on that data within one unit
# Polymorphism - Same method  name behaving differently in differenet classes



class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks")



an1 = Animal('Dog')
an1.speak()

dog1 = Dog('Monaco')
dog1.speak()


class BankAccount:

    def __init__(self,name:str,amount:float) -> None:
        self.name = name
        self.__balance = amount

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f'Now your balance is {self.__balance}')
        else:
            print('Amount should be positive')
    
    def show_balance(self):
        print(f'Your balance is {self.__balance}')
        self.__rotation()

    def __rotation(self):
        print('Rotate in next month')

acc = BankAccount('John',500)
acc.deposit(100)
acc.show_balance()
print(acc.name)
# print(acc.__balance)
# acc.__rotation()

