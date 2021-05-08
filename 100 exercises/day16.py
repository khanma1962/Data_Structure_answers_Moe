'''
Question 60
Question
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
500
'''
def compute_func(n):
    if n == 0:  # boundary case
        return 0
    return compute_func(n-1) + 100
# print(compute_func(5))
'''
Question 61
Question
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
13
'''
def fib(n):
    if n < 2 :  # boundary condition
        return n
    return fib(n-1) + fib(n-2)

for i in range(20):
    # print(fib(i), end = '   ')
    pass
'''
Question 62
Question
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7
Then, the output of the program should be:

0,1,1,2,3,5,8,13
'''
def fib2(n):
    if n < 2 : # boundary condition
        return n
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a , b = b, a + b

# for x in fib2(7):
    # print(x, end = '   ')

'''
Question 63
Question
Please write a program using generator to print the even numbers between 0 and n in comma separated 
form while n is input by console.

Example: If the following n is given as input to the program:
10
Then, the output of the program should be:

0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def gen_num(n):
    for i in range(n+1):
        if not (i % 2):
            yield  i

# for num in gen_num(10):
#     print(num, end = ' ')

'''
Question 64
Question
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 
and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

100
Then, the output of the program should be:

0,35,70
'''
def  gen_5_7(n):
    for i in range(n+1):
        if not ( (i % 5) or (i % 7)):
            yield i
for num in gen_5_7(101):
    print(num, end = ",  ")

    
