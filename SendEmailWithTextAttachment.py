# Import smtplib for the actual sending function
import smtplib
# Here are the email package modules we'll need
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
# Import datetime for timestamp 
from datetime import datetime

# Generate timestamp
now = datetime.now()
timestamp = str('%s/%s/%s_%s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

#recipient == recipient's email address
#sender == my email address & password == password for sender account
recipient = 'sample_recipient@gmail.com'
sender = 'sample_sender@gmail.com'
password = 'sample_password'
subject = 'API Test Results ' + str(timestamp)

try:
	# Create the container email message
	msg = MIMEMultipart()
	msg['Subject'] = subject
	# Attach the file
	msg.attach(MIMEText(file('Result_file.txt').read()))
		 
	# Specify host & port for gmail
	smtpserver  = smtplib.SMTP("smtp.gmail.com",587)
	# Identify yourself to an SMTP server using EHLO
	smtpserver.ehlo()
	smtpserver.starttls()
	# Log in on an SMTP server that requires authentication
	smtpserver.login(sender, password)
		 
	# Terminate the SMTP session and close the connection
	smtpserver.sendmail(sender, recipient, msg.as_string())
	smtpserver.quit()
	print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
