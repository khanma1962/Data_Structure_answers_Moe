'''
Question 31
Question:
Define a function which can print a dictionary where the keys are numbers between
1 and 20 (both included) and the values are square of keys.
'''

def print_dict(start = 1, end = 20):
    d = {}
    for i in range(start, end+1):
        # print(i)
        d[i] = i ** 2

    print(d)

# print_dict()

'''
Question 32
Question:
Define a function which can generate a dictionary where the keys are numbers 
between 1 and 20 (both included) and the values are square of keys. The function 
should just print the keys only.
'''

def print_dict2(start = 1, end = 20):
    d = {}
    for i in range(start, end+1):
        # print(i)
        d[i] = i ** 2

    for j in d.keys():
        print(j, end = " ")

    print('\n')
    for j in d.values():
        print(j, end = " ")

# print_dict2()

'''
Question 33
Question:
Define a function which can generate and print a list where the values are square of 
numbers between 1 and 20 (both included).
'''

def print_list(start = 1 , end = 20):
    lst = []
    for i in range(start, end + 1):
        lst.append(i ** 2)
    print(lst)

# print_list()

'''
Question 34
Question:
Define a function which can generate a list where the values are square of numbers 
between 1 and 20 (both included). Then the function needs to print the first 5 elements 
in the list.
'''

def print_list(start = 1 , end = 20):
    lst = []
    for i in range(start, end + 1):
        lst.append(i ** 2)

    for i in range(5):
        print(lst[i], end = ' ')

# print_list()

'''
Question 35
Question:
Define a function which can generate a list where the values are square of numbers 
between 1 and 20 (both included). Then the function needs to print the last 5 elements 
in the list.
'''
def print_list(start = 1 , end = 20):
    lst = []
    for i in range(start, end + 1):
        lst.append(i ** 2)

    for i in range(5):
        print(lst[len(lst) - i - 1], end = ' ')
        # print(lst[-i:])
    print(lst[-5:])


# print_list()

'''
Question 36
Question:
Define a function which can generate a list where the values are square of numbers 
between 1 and 20 (both included). Then the function needs to print all values except 
the first 5 elements in the list.
'''
def print_list(start = 1 , end = 20):
    lst = []
    for i in range(start, end + 1):
        lst.append(i ** 2)

    for i in range(5, len(lst)):
        # print(i)
        print(lst[i], end = ' ')
        # print(lst[-i:])
    print(lst[5:])


# print_list()

'''
Question 37
Question:
Define a function which can generate and print a tuple where the value are square of 
numbers between 1 and 20 (both included).
'''
def print_tuple(start = 1, end = 20):
    lst = []
    for i in range(start, end + 1):
        lst.append(i ** 2)

    print(tuple(lst))

print_tuple()


