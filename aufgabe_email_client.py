import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sending():
    # assign key email aspects to variables for easier future editing
    subject = "Betreff"
    body = "Inhalt"
    sender_email = "deine@mail.de"
    receiver_email = ["empfaenger1@mail.de", "empfaenger2@mail.de"]
    file = "report.pdf" # in the same directory as script
    password = "passwort123"

    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = ", ".join(receiver_email)
    email["Subject"] = subject

    # Add body and attachment to email
    email.attach(MIMEText(body, "plain"))
    attach_file = open(file, "rb") # open the file
    report = MIMEBase("application", "octate-stream")
    report.set_payload((attach_file).read())
    encoders.encode_base64(report)

    #add report header with the file name
    report.add_header("Content-Decomposition", "attachment", filename = file)
    email.attach(report)

    #Create SMTP session for sending the mail

    session = smtplib.SMTP('smtp.strato.de', 587) #use strato with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent')