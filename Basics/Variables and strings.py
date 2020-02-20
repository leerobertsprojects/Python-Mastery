#Variables
# iq = 190
#
# print(iq * 5)
# print(type(iq))

# Strings

single_string = 'Hello World'
double_string = " Hello World"
long_string = '''
Hello multiline
string '''
print(single_string, double_string)
print(long_string)

print(single_string + ' ' + double_string)

print(str(100) + ' Bottle of beer on the wall')

print('Hello\nWorld')
string_a = 'Hello'

string_b = 'World'
print(f'{string_a} {string_b}') #new way called fstrings and prefered way in new versions of python
print('{1} {0}'.format(string_a, string_b)) # old way but can use index numbers to swap values around

shelfish = 'me me me'

print(shelfish[1:8:2])  # start:stop:step over
print(shelfish[3:])  # start at 3 and go to the end
print(shelfish[:4])  # starts at the beginning and ends at 4
print(shelfish[::1])  # prints the whole thing
print(shelfish[::-1])  # reverses the string

print(len(shelfish))
print(shelfish.capitalize())

