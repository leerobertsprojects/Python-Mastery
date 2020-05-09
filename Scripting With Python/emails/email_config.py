import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('content.html').read_text())
email = EmailMessage()
email['from'] = 'Lee Roberts'
email['to'] = 'leesroberts@virginmedia.com'
email['subject'] = 'Do You like Python'
email.set_content(html.substitute(name='Lee'), 'html')

''' use the template module so 
you can use variables in the email content '''



with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('leeroberts1701@gmail.com', 'ryan1701')
    smtp.send_message(email)
    print('email has been sent!')


