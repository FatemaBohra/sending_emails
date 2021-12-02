import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Fatema Bohra'
email['to'] = 'fatema.bohra2003@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content('I am a python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('fatema.bohra2003@gmail.com', 'fatemabohra123')
    smtp.send_message(email)
    print("All good boss!")
