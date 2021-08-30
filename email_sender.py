
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import ssl
import smtplib
import csv

# Change these variables
SMTP_HOST = "smtp.gmail.com"
SMTP_USERNAME = "eisha.mazhar19@gmail.com"
SMTP_PASSWORD = ""
SENDER_EMAIL = "eisha.mazhar19@gmail.com"
SENDER_NAME = "Eisha Tir Raazia"
BODY ="""Hi -<br><br/>
Thank you for being a huge part of Local Hack Day: Share (2020) by PWiC, Karachi! We are so happy you spent your day building and demoing at Local Hack Day. We wanted to make sure you get recognized for attending as well. You can print out your certificate below to share with your school.<br>
<br>
They can also claim the free Azure credits, Adobe XD, or other resources until then.<br>
<a
    href="https://share.devpost.com/">🏆 Devpost Submissions
</a><br>
<a
    href="https://localhackday.mlh.io/share/workshops">🎓 Workshops
</a><br>
<a
    href="https://azure.microsoft.com/en-us/free/students/">🚩 $100 Azure Credits
</a><br>
<a
    href="https://mlh.az1.qualtrics.com/jfe/form/SV_ePRi23xdJG1iCq1">🚩 Free Adobe XD For Students
</a><br>
<a
    href="https://education.github.com/pack">🚩 GitHub Student Developer Pack
</a><br>
<br>
Link to the resources (slides and code that were presented in sessions): <a href="https://drive.google.com/drive/folders/150vTilq7iGNduSVYHPKRispLjwPKBo0z?usp=sharing">Resources Link</a></a><br>
<br>
<a href="https://www.facebook.com/pakistaniwomenincomputing/">PWiC's page link, Click here!</a><br>
<br>
<a href="https://www.youtube.com/watch?v=Ze0YSQHM16o&t=9172s">Session's YouTube link, Click here!</a><br><br/>
We would love to hear about your experience. Hope to see you next time!<br>
<br>
Happy Hacking,<br>
<br>
Team PWiC, Karachi."""

SUBJECT = "Thank you for attending Local Hack Day: Share; by PWiC, Karachi!"

thankYou='ThankYou.gif'
iDemoed='I_Demoed.gif'

def send_email(name, email, filename):
    RECEIVER_NAME = name
    RECEIVER_EMAIL = email

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = str(Header(SENDER_NAME+' <' + SENDER_EMAIL + '>'))
    message["To"] = str(Header(RECEIVER_NAME+' <' + RECEIVER_EMAIL + '>'))
    message["SUBJECT"] = SUBJECT
    # message["Bcc"] = RECEIVER_EMAIL  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(BODY, "html"))

    # Open PDF file in binary mode
    with open('./filled/' + filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    with open('./'+thankYou, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {thankYou}",
    ) 
    message.attach(part)
    with open('./' + iDemoed, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {iDemoed}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)



    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, 465, context=context) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)



csv_data = csv.reader(open('processed.csv'))
for i, row in enumerate(csv_data):
    send_email(row[0], row[1], row[2])
    print("Email sent to: " + row[1] + ", please remove this row from CSV before re-running script again (in case of any failure)")
