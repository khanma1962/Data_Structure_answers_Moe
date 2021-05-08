'''
Question 16
Question:
Use a list comprehension to square each odd number in a list. The list is input
by a sequence of comma-separated numbers. >Suppose the following input is supplied
to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81

'''

def q16(lst):
    res = []
    for i in lst:
        if i % 2 != 0:
            res.append(i**2)
            print(i**2, end = ' ')
a =[1,2,3,4,5,6,7,8,9]
# q16([1,2,3,4,5,6,7,8,9])

lst = [ i ** 2 for i in a if i % 2]
# print(lst)

'''
Question 17
Question:
Write a program that computes the net amount of a bank account based a transaction 
log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
'''
def q17():
    total = 0
    while True:
        val = input('Please input your transaction')
        if val:
            if val[0] == 'D':
                total += int(val[2:])
                # print('dep', total)
            elif val[0] == 'W':
                total -= int(val[2:])
                # print('withdraw', total)
        else:
            break
    print(total)

# q17()









