import smtplib as s

username = raw_input("Gmail Username: ")
password = raw_input("Gmail Password: ")
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
v_email = raw_input("Email: ")
email_message = raw_input("Message: ")
obj.sendmail(username, v_email, email_message)