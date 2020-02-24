# # functions
#
# # Blocks of code we can reuse.
#
# def greeting():
#     print('Hello World')
#
# greeting()
#
# # default Parameters
# def say_hello(name='default_user'):
#     print(f'Hello {name}')
#
# # Positional Arguments, the positions of the arguments match the way they were defined
#
# say_hello('lee')
#
# # Keyword arguments, You can put them in any order as long as the variable name matches and python will place them (not best practice)
#
# say_hello(name='lee')

def add(*args):
    print(args)


print(add(1, 2, 3, 4, 5))








