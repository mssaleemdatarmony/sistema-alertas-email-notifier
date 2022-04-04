import smtplib

def send_email(sender, sender_pass, subject, body, receiver=None):
    """
        Sends email using pre-configured sender email address.
        :param sender str: Sender's email. 
        :param sender_pass str: Sender's password.
        :param subject str: subject of email.
        :param body str: body of email. 
        :param receiver str: Optional. Receiver's email. (If not provided, sends to sender's email.)
        
    """
    
    email_receiver = receiver if receiver is not None else sender
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, sender_pass)
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(sender, email_receiver, msg=msg)