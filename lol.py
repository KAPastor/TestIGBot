import smtplib


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
