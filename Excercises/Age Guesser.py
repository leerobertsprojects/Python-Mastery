

while True:
    age = int(input('Please Guess My Age: '))

    if age > 38:
        print('Im Not that old try again')
        print('Try a lower age')
        continue
    elif age < 38:
        print('Thanks but im not that young')
        print('Try a higher age')
        continue
    else:
        print('Well Done you guessed correctly')
        break

