'''
Question 22
Question:
Write a program to compute the frequency of the words from the input. The output should
output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1


'''

def compute_word_freq(s):
    d = {}
    words = [x for x in s.split(' ')]

    for word in words:
        # # print(word)
        d[word] = d.get(word, 0) + 1

    print(d)

# compute_word_freq('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')

'''
Question 23
Question:
Write a method which can calculate square value of number
'''
def sq_num(n):
    return n ** 2
# print(sq_num(5))

'''
Question 24
Question:
Python has many built-in functions, and if you do not know how to use it, you can read 
document online or find some books. But Python has a built-in document function for every 
built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), 
int(), raw_input()

And add document for your own function
'''
# print(abs.__doc__)
# print(int.__doc__)
# print(sorted.__doc__)

'''
Question 25
Question:
Define a class, which have a class parameter and have a same instance parameter.
'''

class employee():
    id = 1234  # class parameter
    def __init__(self, id = None):
        self.id = id  # instance parameter

jack = employee(4567)
print(jack.id)

ann = employee()
ann.id = 999
print(ann.id)

