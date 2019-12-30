import smtplib


EMAIL_ADDRESS = 'avery.mitch651@gmail.com'
EMAIL_PASSWORD = 'Saxdude135!'


def create_and_send_email(subject, msg, recv_email=EMAIL_ADDRESS):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, recv_email, message) #change second email to email to send to 
        server.quit()
        print('Success')
    except: 
        print('Failed to send email')


if __name__ == "__main__":
    subject = input('Subject of email: ')
    message = input('Message of email: ')
    to = input('To: ') 
    if to != 'None':
        create_and_send_email(subject, message, to) 
    else:
        create_and_send_email(subject, message)  