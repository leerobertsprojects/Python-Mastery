list = [1, 1, 2, 3, 4, 5, 4, 6, 8, 2, 1, 6,]
dup_list = []

for item in list:
    if list.count(item) > 1:
        if item not in dup_list:
            dup_list.append(item)

print(dup_list)
        

