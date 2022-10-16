import smtplib
from email.message import EmailMessage


def send_me():

    msg = EmailMessage()
    msg.set_content("please oh please just send")

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'Help'
    msg['From'] = "abigailhendrick96@gmail.com"
    msg['To'] = "abigail@abigailhendrick.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost', 1025)
    s.send_message(msg, 'abigailhendrick96@gmail.com', 'abigail@abigailhendrick.com')
    s.quit()


if __name__ == '__main__':
    send_me()
