# Everything in python is an object using classes

class PlayerCharacter:

    # Class Object attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Run(self):
        return self


player1 = PlayerCharacter('Lee', 38)
print(player1.Run())
print(dir(player1))


