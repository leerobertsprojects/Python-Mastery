class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('tabby', 10)
cat2 = Cat('tom', 4)
cat3 = Cat('moggy', 15)

def oldest_cat(*args):
  return max(args)

print(f'The Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old!')
