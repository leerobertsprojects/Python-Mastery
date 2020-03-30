try:
    print(1+'String')
except TypeError:
    print('You had an error')
finally:
    print('Try Again')

def number(num):
    try:
        result = 5 / num
        return result
    except ZeroDivisionError:
        print('You cannot divide by zero')

print(number(0))

