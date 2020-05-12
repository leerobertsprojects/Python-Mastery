from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'get from twilio'
auth_token = 'get from twilio'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This ia reminder.",
                     from_='+447476553473',
                     to='+447976767235'
                 )

print(message.sid)

