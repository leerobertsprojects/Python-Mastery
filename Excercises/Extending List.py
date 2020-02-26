class SuperList(list):

    def __len__(self):
        return 1000



superlist = SuperList()

print(len(superlist))
superlist.append(5)
print(superlist[0])
superlist.append(6)
print(superlist[1])
print(type(superlist))
