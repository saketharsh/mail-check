# -*- coding: utf-8 -*-
"""Command line execution of mail-check """
import argparse
import sys
import os
import mail_check.engine




home = os.path.expanduser("~")

def main(): 
	argparser = argparse.ArgumentParser(description="mail_check")
	argparser.add_argument("-gh","--version", action="store_true",default= False)
	argparser.add_argument("-v","--version", action="store_true",default= False)
	argparser.add_argument("-e","--version", action="store_true",default= False)
	args = argparser.parse_args()
	process(args)


def process(args):
	if args.v:
		detailed_usage()
		sys.exit(2)
	if args.version:
		import release
		print(release.__version__)
		sys.exit(2)










def detailed_usage():
	print("Welcome to documentation of mail-check!")
	image = '''
               .__.__                   .__                   __    
  _____ _____  |__|  |             ____ |  |__   ____   ____ |  | __
 /     \\__  \ |  |  |    ______ _/ ___\|  |  \_/ __ \_/ ___\|  |/ /
|  Y Y  \/ __ \|  |  |__ /_____/ \  \___|   Y  \  ___/\  \___|    < 
|__|_|  (____  /__|____/          \___  >___|  /\___  >\___  >__|_ \
      \/     \/                       \/     \/     \/     \/     \/
	
	'''
	print(image)
	print ("mail-check is a command line tool to read inbox mails,\n")
	print ("and download attachments as and when required \n")
	print("Examples : ")
	print("\t\t1. mail-check")
	print("\t\t2. Enter username >>")
	print("\t\t3. Enter password >>")
	print("\t\t4. List of top 10 unread email appears")
	print("\t\t5. Select the one you want to read, Voila !! It done")
	print("")
	print("Report (and track process on fixing) bugs on " +
	      "https://github.com/saketharsh/mail-check. Or simply write a mail " +
	      "to Saket Harsh at sharsh[at]iit[dot]ac[dot]in")





