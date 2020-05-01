import re
pattern = re.compile(r'[A-Za-z0-9@#$%]{8,}\d') # at least 8 characters long, contains and uppercase letter and numbers and 4 special characters and must end with a number

password = 'hello%aaa1'



if pattern.fullmatch(password):
    print('This password meets complexity well done')

else:
    print('This password does not meet the complexity requirements please try again')
