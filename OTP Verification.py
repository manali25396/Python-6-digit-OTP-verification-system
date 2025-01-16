import random      #to generate random 6 digit otp
import smtplib     # liabrary to send an email
from email.message import EmailMessage    #liabrary to send message in an email

#Used for loop to regenrate new 6 digit OTP everytime
otp=""
for i in range (6):
    otp+=str(random.randint(0,9)) #concatenate everytime inside this loop

#print(otp)


  #created a server to login to an email from which we need to send an email
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login("manalideshmukh25396@gmail.com","zqfw emov vboq zzfa") #Google app password
to_mail= input("Enter your email:")

  #created an object of message to be sent on an email
from_mail="manalideshmukh25396@gmail.com"  #created a variable
msg=EmailMessage()
msg["subject"]="OTP Verification"
msg["From"]= from_mail
msg["To"]= to_mail
msg.set_content("Your OTP is: "+otp)  #Need to set content of the mail

server.send_message(msg)

print("Email sent")



  #To verify the OTP sent on an email
input_otp= input("Enter your OTP: ")
if input_otp==otp:
      print("OTP Verified")
else:
      print("Invalid OTP")



