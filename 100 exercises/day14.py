'''
Question 51
Question
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

def compute():
    while True:
        n = input('Please input a number  :')
        try:
            x = int(n) / 0
        except ZeroDivisionError:
            print(' Divide by zero')
        else:
            print('All done')
            break

# compute()

'''
Question 52
Question
Define a custom exception class which takes a string message as attribute.
'''
class MyError():
    '''
    This  class will display the error message
    '''
    def __init__(self, message):
        self.message = message

e = MyError(' Something is wrong')
# print(e.message)

''''
Question 53
Question
Assuming that we have some email addresses in the "username@companyname.com" format, please 
write program to print the user name of a given email address. Both user names and company names 
are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def decode_email():
    while True:
        info = input('Please input the email address  :  ')
        if info:
            words = info.split('@')
            print(words[0])
        else:
            break

decode_email()




