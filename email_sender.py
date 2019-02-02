import smtplib


def send(email_content):
    fromx = 'tomasz.molenda.sms.backup@gmail.com'
    to = 'tomasz.molenda@gmail.com'
    subject = 'Mam wycieczkę!'  # Line that causes trouble
    msg = 'Subject:{}\n\n{}'.format(subject, email_content)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login('tomasz.molenda.sms.backup@gmail.com', '*D=6;0U549Df_\'%ihg_R')
    server.sendmail(fromx, to, msg.encode('utf-8').strip())
    server.quit()
