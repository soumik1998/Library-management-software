import smtplib
import datetime
from datetime import timedelta
now=datetime.datetime.now()
now=str(now.strftime("%d-%m-%Y"))
def autoremindermail():
    
    fp=open("books_studentsissued.txt","r")
    for i in fp:
        if str(i.split()[10])==now:
            t=str(i.split()[3])
        #print(i.split()[3])
            text=i
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("miarcmalkovarandi@gmail.com", "madarchod")
            server.sendmail("miarcmalkovarandi@gmail.com",t, text)
            server.close()

autoremindermail()      
    
