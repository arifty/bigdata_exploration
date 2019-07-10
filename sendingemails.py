# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
# setup the parameters of the message
password = ""
msg['From'] = "cdl_cloudera@carrefour.com"
msg['To'] = "mahmoodarif_thayal@carrefour.com"
msg['Subject'] = "Photos"

## setup the parameters of the message
#password = "Bautha838#"
#msg['From'] = "arif.ty@gmail.com"
#msg['To'] = "mahmoodarif_thayal@carrefour.com"
#msg['Subject'] = "Photos"
 
# attach image to message body
msg.attach(MIMEImage(file("02_SendingEmails/location3.jpg").read()))
 

# create server
#server = smtplib.SMTP('10.10.4.28: 25')
server = smtplib.SMTP("smtp.gmail.com",587)
 
server.starttls()

server.ehlo()
server.esmtp_features["auth"] = "LOGIN PLAIN"

# Login Credentials for sending the mail
server.login(msg['From'], password)
 

# send the message via the server 
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print "successfully sent email to %s:" % (msg['To'])


# ----------------------------------------


import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText

smtp_server = "10.10.4.28"
port = 25  # For starttls
sender_email = "cdl_cloudera@carrefour.com"
password = ""

# create message object instance
msg = MIMEMultipart()
msg['To'] = "mahmoodarif_thayal@carrefour.com"
msg['Subject'] = "Photos"
# attach image to message body
msg.attach(MIMEImage(file("02_SendingEmails/location3.jpg").read()))

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    #server.starttls(context=context) # Secure the connection
    server.starttls()
    server.ehlo() # Can be omitted
    
    #server.esmtp_features["auth"] = "LOGIN PLAIN"
    server.esmtp_features['auth'] = 'LOGIN DIGEST-MD5 PLAIN'
    server.login(sender_email, password)
    
    # TODO: Send email here
    # send the message via the server 
    server.sendmail(msg['From'], msg['To'], msg.as_string())

except Exception as e:
    # Print any error messages to stdout
    print(e)
    
finally:
    server.quit() 