# Range - useful for for loops and creating lists quickly
for num in range(0, 10):
    print(num)

my_list = list(range(0, 50))
print(my_list)

# Range starts at 0 so a range of 100 will be 0 - 99 bear this in mind

my_reversed_list = list(range(10, 0, -1)) # you have to use a step of -1 to achieve a reverse range otherwise it wont work

print(my_reversed_list)
