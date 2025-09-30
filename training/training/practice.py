"""
Sum of first N natural number (1 to n
"""


# n = 5
# start = 1
# natural_add = 0

# while start < 6:
#     natural_add = natural_add + start
#     start = start + 1

# print(natural_add)

# n = 5
# a = 0

# for i in range(1,n+1):
#     a= a+i

# print(a)

n = input('Enter an natural number : ')
n = int(n)
if n == 0:
    print('Enter input is not natural number')
else:
    a = 0
    for i in range(1,n+1):
        a = a + i

    print('Natural number addition is :',a)