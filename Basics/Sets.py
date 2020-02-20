# # Sets {}
#
# my_set = {1, 2, 3, 4, 4, 6, 7, 7}
#
# print(my_set)
#
# my_list = [1, 2, 2, 3, 4, 4, 5]
#
# print(set(my_list)) # convert list to set to only show unique values
#
# print(2 in my_set)

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set)) # difference between 2 sets
# print(my_set.discard(5)) # discards the value specified in place so does not return anything
# print(my_set)
# print(my_set.difference_update(your_set)) # updates the set with the differences between 2 sets removed
# print(my_set)
print(my_set.isdisjoint(your_set))  # lets you know if the sets if have anything in common, if it has matching values you will get false
print(my_set.union(your_set)) # joins the sets together
print(my_set.issubset(your_set)) # if myset is entirely in your set then my set is a subset of your set
print(your_set.issuperset(my_set)) # if myset encompasses your_set the it is a superset of your_set













