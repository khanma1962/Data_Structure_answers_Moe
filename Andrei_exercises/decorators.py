# Higher Order Function HOC



def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func()



def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***************')
        func(*args, **kwargs)
        print('***************')
    return wrap_func

@my_decorator
def hello(greeting, emoji = ':)'):
    print(greeting, ':)')

# hello('hiii' )


# performace decorator
import datetime
def performance(func):
    def wrap_func(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f'total time taken is {end-start}')
    return wrap_func

@performance
def long_time():
    for i in range(100000000):
        i *5
long_time()

