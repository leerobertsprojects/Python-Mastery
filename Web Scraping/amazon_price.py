from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from time import sleep



def email_me():
    email = EmailMessage()
    email['from'] = 'Lee Roberts'
    email['to'] = 'leesroberts@virginmedia.com'
    email['subject'] = 'Your price has dropped'
    email.set_content(f'The price fell check out https://www.amazon.co.uk/Apple-iPad-Air-16GB-Refurbished/dp/B07GZP1HJM/ref=sr_1_16?dchild=1&keywords=ipad&qid=1589402123&sr=8-16')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('leeroberts1701@gmail.com', 'ryan1701')
        smtp.send_message(email)
        print('email has been sent!')

def get_price():
    web_url = 'https://www.amazon.co.uk/Apple-iPad-Air-16GB-Refurbished/dp/B07GZP1HJM/ref=sr_1_16?dchild=1&keywords=ipad&qid=1589402123&sr=8-16'
    url = requests.get(web_url).text

    amazon = BeautifulSoup(url, 'html.parser')

    price = float(amazon.find('span', id='priceblock_ourprice').text.replace('£', ''))
    print(price)

    if price < 250.00:
        email_me()

while True:
    get_price()
    sleep(3600)






