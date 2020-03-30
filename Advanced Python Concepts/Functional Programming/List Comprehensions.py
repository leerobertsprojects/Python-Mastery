# List Comprehensions

# quick ways to create lists is python

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# there is a quicker way

# my_list = [param for param in iterable]

my_list = [char for char in 'hello']

print(my_list)

# first param can be an expression

my_list2 = [num * 2 for num in range(0, 100)]
print(my_list2)

# Can add a conditional at the end also

my_list3 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list3)