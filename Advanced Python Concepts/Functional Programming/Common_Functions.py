from functools import reduce
# map, filter, zip & reduce
#map

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))

mylist = [2,3,4]


def multiply_by3(item):
    return item*3

def check_odd(item):
    return item % 2 != 0

print(list(map(multiply_by3, mylist)))
print(mylist)
# filter


print(list(filter(check_odd, mylist)))
# it will filter out the what the function asked to check for

# zip

new_list = 'hello'
my_list = 'james'

new_list1 = [1,2,3]
my_list1 = [10,20,30]

print(list(zip(my_list, new_list)))
print(list(zip(my_list1, new_list1)))
#works with any iterable including strings

# reduce
new_list2 = [1,2,3]
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, new_list2, 0))
#reduce reduces multiple values down to a sinlge value




