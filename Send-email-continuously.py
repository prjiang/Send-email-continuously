import email.message
msg = email.message.EmailMessage()
account = str(input('Your account: '))
password = str(input('Your password: '))
msg['From'] = account
msg['To'] = str(input('Recipient\'s account: '))
msg['Subject'] = str(input('Subject: '))
msg.set_content(str(input('Content: ')))

import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(account, password)

n = int(input('How many times: '))
i = 0
while i < n:
    server.send_message(msg)
    i += 1
print('success!')
server.close()
# 使用完建議關閉允許低安全性應用程式存取權
