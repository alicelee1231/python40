import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

send_emil = "saemmilee1231@gmail.com"
send_pwd = "vyut wydi nrbx befv"

recv_mail = "sammy342@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg["Subject"] = "this is testing about sending referenced file"
msg["From"]= send_emil
msg["To"] = recv_mail

text = """
please check the referenced file
"""

contentPart = MIMEText(text)
msg.attach(contentPart)
etc_file_path = r'/Users/isaemmi/Desktop/pyProject/13.메일보내기/referenced.txt'

with open(etc_file_path,"rb") as f :
    etc_part = MIMEApplication(f.read())
    etc_part.add_header("Content-Disposition", 'attachment', filename="referenced.txt")
    msg.attach(etc_part)

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_emil, send_pwd)
s.sendmail(send_emil, recv_mail, msg.as_string())
s.quit()
