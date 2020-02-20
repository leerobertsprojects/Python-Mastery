username = input('Please input Username: ')
password = input('Please enter Password: ')
hash = '*' * len(password)

print(f'Hello {username}, Your Password {hash} is {len(password)} letters long.')

