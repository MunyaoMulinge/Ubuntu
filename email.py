import smtplib

sender = "victormunyao96@gmail.com"
receiver = "victormunyao5@gmail.com"
password = "luvuxomuchy"
subject = "Python Email Test"
body = "Wrote Email Using Python"

message = f"""From: Victor Munyao{sender}
To: Munyao Victor{receiver}
Subject: {subject}\n
{body}

"""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # Transport Layer Security

# try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
# except:
