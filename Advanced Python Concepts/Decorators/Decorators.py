# decorators start with an @

def my_decorator(function):
    def wrap_func():
        print('*********')
        function()
        print('*********')
    return wrap_func


@my_decorator
def hello():
    print('Hello World')

hello()

# decorator with arguments and keyword arguments


def my_decorator1(function):
    def wrap_func(*args, **kwargs):
        print('*********')
        function(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator1
def hello1(greeting, emoji=':('):
    print(greeting, emoji)

hello1('hello')

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}s to complete')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5

long_time()




