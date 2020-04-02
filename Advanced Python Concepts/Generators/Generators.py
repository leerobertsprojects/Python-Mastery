# Generators allow us to generate a sequence of numbers over time - range is a kind of generator

# Generators are generally functions


def generator_function(num):
    for i in range(num):
        yield i

# for item in generator_function(1000000):
#     print(item)

g = list(generator_function(1001))

print(g)
# This is a function that will take up a lot of memory to run


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
