import re

text = 'this is some text and this is going to used for testing'
a = re.search('this', text)
if a:
    print(a.span())  # this will give the index number of when the match starts and when it ends
    print(a.start())  # this will give only the index where the match starts
    print(a.end())  # this will the index of where the match ends
    print(a.group())  # this will return the whole matched section
else:
    print('There is no match')

pattern = re.compile('^this') # this will allow you to search against a specific pattern see below
b = pattern.findall(text)  # we just have to pass the variable with the text we wish to search now without creating multiple match objects
print(b)
c = pattern.fullmatch(text)
print(c)
d = pattern.match(text)
print(d)


