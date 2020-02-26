class ActionFigure:
    def __init__(self, toy, age):
        self.toy = toy
        self.age = age
        self.mydict = {
            'soldier' : 'green',
            'car' : 'red'
        }

    def __len__(self):
        return 10
    def __str__(self):
        return 'This is a string'
    def __call__(self, *args, **kwargs):
        return 'This run with the brackets'

    def __getitem__(self, i):
        return self.mydict[i]




actionfigure1 = ActionFigure('Action Figure', 0)

print(len(actionfigure1))
print(str(actionfigure1))
print(actionfigure1())
print(actionfigure1['soldier'])

