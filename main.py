import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dateutil import relativedelta

print("Script started")

months = relativedelta.relativedelta(datetime.now(), datetime(2022, 7, 1)).months
msg = EmailMessage()

msg.set_content(f'''{os.getenv("FIO")}
{os.getenv("ADDRESS")}
Лицевой счет {os.getenv("ACCOUNT")}
Кухня:
ГВС - {44 + months * 2}
ХВС - {123 + months * 2}
Сан. узел:
ГВС - {101 + months * 2}
ХВС - {261 + months * 2}
 
89О4676O579''')

msg['Subject'] = os.getenv("ADDRESS")
msg['From'] = os.getenv("mail-mine")
msg['To'] = os.getenv("mail-send")

print("Message prepared")

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.getenv("mail-mine"), os.getenv("psw"))
server.send_message(msg)
print("message sent")
server.quit()
print("server quit")
