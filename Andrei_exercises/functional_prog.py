# map, filter, zip, and reduce

def multiply_by2(lst):
    lst_by2 = []
    for i in lst:
        lst_by2.append(2 * i)
    return lst_by2


# print(multiply_by2([9, 4, 8]))

my_list = [3, 9, 12, 17, 21, 20]


def multiply_by2_new(items):
    return 2 * items


# print(list(map(multiply_by2_new, my_list)))
# print(my_list)

def check_odd(items):
    return items % 2


# print(list(filter(check_odd, my_list)))


a = [3, 9, 12, 17, 21, 20]
b = [4, 6, 1, 90, 65, 9]

# print(list(zip(a, b)))

from functools import reduce

# print(reduce(lambda a, b: a+b, my_list))
# print(reduce(lambda a, b: a if a > b else b, my_list))

lst = [99, 29, 43]


def accumulator(acc, items):
    print(f'acc is {acc} and itmes are {items}')
    return acc + items


print(reduce(accumulator, lst, 0))
