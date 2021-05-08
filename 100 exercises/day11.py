'''
Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half
values in one line and the last half values in one line.
'''

def print_tuple(t):
    # print(t[:5])
    # print(t[5:])
    for i in range(0, round(len(t)/2)):
        print(t[i], end = ' ')

    print('\n')
    for i in range(round(len(t)/2), len(t)):
        print(t[i], end = ' ')


t = (1,2,3,4,5444,6,7,8,9,10)
# print_tuple(t)

'''
Question 39
Question:
Write a program to generate and print another tuple whose values are even numbers 
in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''
def print_another_tuple(t):
    lst = []
    for i in t:
        lst.append(i ** 2)
    print(tuple(lst))

t = (1,2,3,4,5,6,7,8,9,10)
# print_another_tuple(t)

'''
Question 40
Question:
Write a program which accepts a string as input to print "Yes" if the string is 
"yes" or "YES" or "Yes", otherwise print "No".
'''

def print_yes(s):
    if s == 'yes' or s == 'YES' or s == 'Yes':
        print('Yes')
    else:
        print('No')

# print_yes('yEs')

'''
Question 41
Question:
Write a program which can map() to make a list whose elements are square of elements 
in [1,2,3,4,5,6,7,8,9,10].
'''

def sq(n):
    return n ** 2

# res = list(map(sq, [1,2,3,4,5,6,7,8,9,10]))
res = list(map(lambda x: x **2, [1,2,3,4,5,6,7,8,9,10]))
# print(res)

'''
Question 42
Question:
Write a program which can map() and filter() to make a list whose elements are square 
of even number in [1,2,3,4,5,6,7,8,9,10].
'''
def is_odd(n):
    return n % 2

def sq(n):
    return n ** 2


a = [1,2,3,4,5,6,7,8,9,10]
res = list(map(sq, filter(is_odd, a)))
# print(res)

'''
Question 43
Question:
Write a program which can filter() to make a list whose elements are even number between 
1 and 20 (both included).
'''
def filter_list(start = 1, end = 20):
    lst = []
    for i in range(start, end+1):
        if not (i % 2):
            lst.append(i)
    return lst

# res = filter_list()

def is_even(n):
    return not ( n % 2)
# res = list(filter(is_even, [x for x in range(1, 21)]))
res = list(filter( is_even, range(1, 21)))
print(res)



