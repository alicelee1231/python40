import smtplib
from email.mime.text import MIMEText

send_email = "saemmilee1231@gmail.com"
send_pwd = "vyut wydi nrbx befv"

recv_email = "sammy342@naver.com"

smtp_name="smtp.gmail.com"
smtp_port = 587

text= """
I am writing a message here,
and I will become a king of python.
I will earn a lot of money just on my power
and someday, I will work in google.
that someday will be 3years.
"""

msg = MIMEText(text)

msg["Subject"] = "writing the message title"
msg["From"] = send_email
msg["To"] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()
