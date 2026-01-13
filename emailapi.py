import smtplib
import formbackend

results = formbackend
 
email = 'linusngugi4@gmail.com'
receiver = 'mactechkiarie@gmail.com'

subject = 'test'
message= f'{results}'
text = f'Subject: {subject}\n\n{message}'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email, 'nymq netk fodr psta ')
server.sendmail(email,receiver,text)
