# map, filter, zip & reduce

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))

mylist = [2,3,4]


def multiply_by3(item):
    return item*3

print(list(map(multiply_by3, mylist)))
print(mylist)
