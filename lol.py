import smtplib

# you == the recipient's email address
msg['Subject'] = 'The contents of '
msg['From'] = 'kyleanthonypastor@gmail.com'
msg['To'] = 'kyle.pastor@scotiabank.com'

fromaddr = 'kyleanthonypastor@gmail.com'
toaddrs  = 'kyle.pastor@scotiabank.com'
msg = 'Why,Oh why!'
username = 'kyleanthonypastor@gmail.com'
password = ''

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
