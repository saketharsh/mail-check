""" The engine module of mail-check"""

##################################################################################
# mail-check                                                                     #
# python2 script to view mails and download attatchments from terminal           #
# Copyright- Saket Harsh IIT Kanpur                                              #
# E-Mail- sharsh2010@gmail.com                                                   #
##################################################################################



import email, getpass, imaplib, os, urllib2
from termcolor import colored
prompt= ">>"

def mail_function():
	def connectivity():
		try:
			response=urllib2.urlopen('https://webmail2.iitk.ac.in/webmail/src/login.php',timeout=20)
			return 1
		except urllib2.URLError:
			try:
				response=urllib2.urlopen('https://www.google.co.in/',timeout=20)
				return 2
			except urllib2.URLError:
				return False
	    

	if not connectivity():
		print "Check Internet Connection ! Exiting"
		quit()

	server=["newmailhost.cc.iitk.ac.in","qasid.iitk.ac.in"]
	print colored("Enter WebMail username","blue")
	user = raw_input(prompt)
	print colored("Enter Password", "blue")
	pwd = getpass.getpass( prompt)

	# Connecting to WebMail IMAP Server
	m = imaplib.IMAP4_SSL(server[connectivity()-1]) 
	m.login(user,pwd)
	m.select("INBOX")   # You can choose other mailboxes too.
	resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
	items=items[0].split()




	#Printing Top 10 Mails from Inbox
	for emailid in range(1,11):	
		color=["blue","white"]
		resp, data = m.fetch(items[len(items)-emailid], "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, 
		email_body = data[0][1] # getting the mail content
		mail=email.message_from_string(email_body)
		sender = mail['from'].split()[-1]
		print emailid , colored(mail['Subject'], color[emailid%2])
		print colored(sender, color[emailid%2])
		


	# Taking User Input to show the Mail 
	print colored("\nEnter Mail Number","cyan")	
	mail_num=int(raw_input(prompt))
	os.system("clear")   # Clear the screen to show fresh mail		
	resp, data = m.fetch(items[len(items)-mail_num], "(RFC822)") 
	email_body = data[0][1] 
	mail=email.message_from_string(email_body)


	# Two cases arise Either mail is multipart(probably Containing attatchments) or text. Dealing both differently
	if mail.is_multipart():
		bodytext=mail.get_payload()[0].get_payload();
		if type(bodytext) is list:
			bodytext=','.join(str(v) for v in bodytext)
		print "\n\n\n\n"
		print(' MESSAGE'.center(80, '*')), "\n"
		print "Subject:-" , mail['Subject']
		print "\n\n"
		print bodytext
	else:
		print "\n\n\n\n"
		print(' MESSAGE '.center(80, '*')) , "\n"
		print "Subject:-" , mail['Subject']
		print "\n\n"
		print mail.get_payload()
		

	# To download attachments if available
	for part in mail.walk():
	        if part.get_content_maintype() == 'multipart':
	            continue
	        if part.get('Content-Disposition') is None:
	            continue
	        filename = part.get_filename()
	        if filename != "untitled-[2].html":   # Default name of an untitled file that is never needed to be Downloaded 
	        	print filename 
	        	print "To Download press Y or y"
	        	attach= raw_input(prompt)
	        	if attach is "y" or "Y":
	        		data = part.get_payload(decode=True)
	        		if not data:
	        			print 'No attachments...'
	        			continue
	        			f  = open( os.path.join( "~/Downloads",filename), 'w')
	        			f.write(data)
	        			f.close()
	        	else:
	        		print ("Exiting!")	
	m.close()
	m.logout()
