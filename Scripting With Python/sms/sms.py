from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9969ea50ffadcaaafa8f107940656d81'
auth_token = '2a6749e344c05f86a16c1057fd9f9a86'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This ia reminder.",
                     from_='+447476553473',
                     to='+447976767235'
                 )

print(message.sid)

