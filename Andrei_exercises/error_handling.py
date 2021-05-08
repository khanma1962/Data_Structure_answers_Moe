# Error Handling
# https://docs.python.org/3/library/exceptions.html
while True:
    try:
        age = int(input('What is your age  :'))
        print(10/age)
        # raise ValueError('Cut it out')
    except ValueError:
        print('Please enter the age in numbers')
    except ZeroDivisionError:
        print('Please enter the age in numbers greater than 0')
    else:
        print('Thank you')
        break
    # finally:
    #     print('OK, I\'m finally done')

# def sum(n1, n2):
#     try:
#        return n1 / n2
#     except (TypeError, ZeroDivisionError) as err:
#         print( err)
#
#
# print(sum(1,0))

