# One time anonymous functions you use only once

# lambda param: action(param)

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))
print(my_list)

square_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, square_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

