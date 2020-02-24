def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

def highest_odd(li):
    odds = []
    for item in li:
        if item % 2 == 1:
            odds.append(item)
    return max(odds)

print(highest_odd([1,2,3,4,5,6,7,8,9,25,33]))

print(highest_even([1,2,3,4,5,6,7,8,9,25,33]))




