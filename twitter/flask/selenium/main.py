import os
import sys
video_name = sys.argv[1]
download = "you-get %s"%video_name
os.system(download)
gg=""
for i,j,k in os.walk('./'):
    for file in k:
        if file.endswith('.mp4'):
            gg=os.path.join(i,file)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = "tian.r.king@gmail.com"
password = "vuuaqdjdbvtfpabr"
mail_from = "tian.r.king@gmail.com"
mail_to = "tianrking@yahoo.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"
mail_attachment=gg
mail_attachment_name=str(gg)[2:]

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))

with open(mail_attachment, "rb") as attachment:
    mimefile = MIMEBase('application', 'octet-stream')
    mimefile.set_payload((attachment).read())
    encoders.encode_base64(mimefile)
    mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
    mimemsg.attach(mimefile)
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()

os.system("rm -rf *mp4 *srt")
