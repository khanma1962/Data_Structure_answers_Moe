'''
Question 14
Question:
Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9

'''

def q14(s):
    dict = {'upper case': 0 , 'lower case': 0}
    s.split(' ')
    # print(s)
    for i in s:
        # print(i)
        if i.islower():
            dict['lower case'] += 1
        if i.isupper():
            dict['upper case'] += 1
    print('Upper Case : ', dict['upper case'])
    print('Lower Case :' , dict['lower case'])


s = 'Hello world!'
# q14(s)

'''
Question 15
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit 
as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:
11106

'''
def q15(num):
    total, res = '', 0
    for i in range(4):
        total += (str(9))
        res += int(total)
    print(res)

q15(9)






