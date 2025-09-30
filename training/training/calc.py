def menu() -> None:
    options : list[str] = [
        'Please choose an operation  below according index number: ',
        '1. Addition',
        '2. Subtraction'
    ]
    for option in options:
        print(option)


def valid_option_input() -> int | None:
    try:
        op = int(input('\n ->  '))
        return op
    except:
        print('Please enter the valid input...')

def valid_calc_input() -> tuple[int] | tuple[None]:
    try:
        fn = float(input('Please enter first number : '))
        sn = float(input('Please enter second number : '))
        return fn, sn
    except:
        print('Please enter the value int.')
        return None, None

def add(num1:float,num2:float)->float:
    return num1 + num2

def sub(num1:float,num2:float)->float:
    return num1 - num2

def calc():
    menu()
    inp = valid_option_input()
    num1,num2 = valid_calc_input()
    result = None
    match inp:
        case 1:
             result = add(num1,num2)
        case 2:
            result = sub(num1,num2) 
        case _:
            print('Operation is not available...')
    print('Your result is : ',result)

calc()
    
