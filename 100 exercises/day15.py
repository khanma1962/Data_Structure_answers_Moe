'''
Question 54
Question
Assuming that we have some email addresses in the "username@companyname.com" format, please
write program to print the company name of a given email address. Both user names and company names
are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def decode_email():
    while True:
        info = input('Please input the email address  :  ')
        if info:
            words = info.split('@')
            email = words[1].split('.')
            print(email[0])
        else:
            break
# decode_email()

'''
Question 55
Question
Write a program which accepts a sequence of words separated by whitespace as input to print the words 
composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']
'''
import re
s = '2 cats and 3 dogs. 455 animals 90 people'
ans = re.findall(r'\d+', s)
# print(ans)

res = [int(x) for x in s.split(' ') if x.isdigit()]
# print(res)

'''
Question 56
Question
Print a unicode string "hello world".
'''
a_string = "This is a unicode string :)"
# print(type(a_string))
#
# a_string = a_string.encode('utf-8')
# print(a_string)
# print(type(a_string))
#
# a_string_again = a_string.decode('utf-8')
# print(a_string_again)
# print(type(a_string_again))

'''
Question 57
Question
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
'''
s = 'hello world'
print(type(s))
s = s.encode('utf-8')
print(type(s))
'''
Question 58
Question
Write a special comment to indicate a Python source code file is in unicode.
'''
# - * -coding: utf-8 -*-
'''
Question 59
Question
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
'''
def  compute_series(n):
    res, top, bot = 0, 1,2
    while top <= n:
        res += top/bot
        top += 1
        bot += 1
    return res

print(compute_series(5))





