import ssl

from twilio.rest import Client
import smtplib
MY_MAIL="mailtobobysharma@gmail.com"
MAILPASS="bobmerimarlo"
TWILOSID="AC04f213f196d0db2b5b709b9c5b6cd061"
TWILIOAUTH="227f932f1095261a7fc5040b76752512"
MYTWILIONO="+18573746635"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def sendsmsalart(self,sms):
        client = Client(TWILOSID, TWILIOAUTH)
        message = client.messages.create(
            body=sms,
            from_=MYTWILIONO,
            to='+919834343800'
        )

        print(message.status)

    def sendemail(self,maillist,flight_offer):
        port = 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as connection:
            #connection.starttls()
            connection.login(user=MY_MAIL,password=MAILPASS)
            for address in maillist:
                connection.sendmail(from_addr=MY_MAIL,to_addrs=address,msg=f"Subject:Flight deal!"
                                                                           f"{flight_offer}")
