# set and dictionary comprehensions

# set comprehentions same as list exeprt use curly brackets

my_set = {char for char in 'hello'}#
print(my_set)

# Dictionary Comprehensions
simple_dict = {
    'a': 2,
    'b': 4
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}

print(my_dict)

# uses the num variable for the key and values

my_dict1 = {num: num*2 for num in [1, 2, 3]}
print(my_dict1)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)