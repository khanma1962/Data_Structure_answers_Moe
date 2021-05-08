# iterable
# __iter__

def generator_function(num):
    for i in range(num):
        yield i**2

# for item in generator_function(100):
#     print(item, end="  ")

g = generator_function(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


