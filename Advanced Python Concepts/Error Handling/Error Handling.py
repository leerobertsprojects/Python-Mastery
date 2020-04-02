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
    finally:
        print('You have fucked up')





print(number(0))



