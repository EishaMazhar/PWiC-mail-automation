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
SMTP_USERNAME = "karachi.chapter@pwic.org"
SMTP_PASSWORD = ""
SENDER_EMAIL = "karachi.chapter@pwic.org"
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