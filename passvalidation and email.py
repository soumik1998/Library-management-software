def passval():
	import getpass
	import re
	
	x = True
	print("Instructions:")
	print("1>At least 1 letter between [a-z] and 1 letter between [A-Z]. ")
	print("2>At least 1 number between [0-9].")
	print("3>At least 1 character from [$#@].")
	print("4>Minimum length 6 characters.")
	print("5>Maximum length 16 charactersss.\n")
	p = getpass.getpass()
	while x:  
		if (len(p)<6 or len(p)>12):
		    break
		elif not re.search("[a-z]",p):
		    break
		elif not re.search("[0-9]",p):
		    break
		elif not re.search("[A-Z]",p):
		    break
		elif not re.search("[$#@]",p):
		    break
		elif re.search("\s",p):
		    break
		else:
		    print("Valid Password") 
		    x=False
		    break
		return True

	if x:
		print("Not a Valid Password") 
		print("Please reenter the pass")
		return False
	print ('You entered:', p)
#passval()
import smtplib
def automali(tosender):
        	
	i=True
	while i:
        	text='its me!!!'

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()

		server.ehlo()

		server.login("udtapunjabgstar@gmail.com", "udtapunjab")
		server.sendmail("udtapunjabgstar@gmail.com", tosender, text)

		server.close()
                i=False 
                	
tosender="shobhit.m16@iiits.in"		
automali(tosender)
