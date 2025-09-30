# If statement

number = 3

if number > 1:
    print('Yes')

if number > 1:
    print('Yes')
else:
    print('No')


if number > 1:
    print('Yes')
elif number == 2:
    print('Unexpected')
else:
    print('No')

n1 = 1
while n1 < 5:
    print('Yes')
    n1 = n1 + 1


# ==
# !=
# < 
# >
# <=
# >=
# and
# or
# not
# in
# is

n2 = '2' 
n3 = 6

if n2 == 2 and n3 == 4:
    print(True)

if n2 == 2 or n3 < 4:
    print(True)

if n2 is 2:
    print('ok')

if 2 not in [1,4]:
    print('I am unique')

if 4 in [1,4]:
    print('I am  not unique')


