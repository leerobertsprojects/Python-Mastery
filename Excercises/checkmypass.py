import requests
import hashlib
import sys


args = sys.argv[1:]

for i in args:
    hash = hashlib.sha1(i.encode('utf-8')).hexdigest().upper()
    url = f'https://api.pwnedpasswords.com/range/{hash[:5]}'
    res = requests.get(url)
    res_list = (res.split(':') for res in res.text.splitlines())
    for h, count in res_list:
        if h == hash[5:]:
            print(f'Your Password {i} has been hacked {count} times, it is not safe to use')

    if hash[5:] not in res.text:
        print(f'your password {i} is safe you may use it.')















