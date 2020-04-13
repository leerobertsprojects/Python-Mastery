import random
import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
attempts = 0
target = random.randint(int(num1), int(num2))
name = input(' What is your name ')
while True:
    attempts += 1
    try:
        guess = int(input(f'Hello {name} please guess a number between {num1} and {num2}: '))
        if guess > int(num2) or guess < int(num1):
            print(f'Please keep your guesses between {num1} and {num2}')

        elif guess > target:
            print('Too High')

        elif guess < target:
            print('Too Low')

        else:
            print('You guessed correctly Well Done')
            print(f'You took {attempts} tries to guess correctly')
            break
    except ValueError:
        print('Please enter a number')



