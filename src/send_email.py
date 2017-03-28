import smtplib, imaplib, email, time, os, re, sys, base64, win32com.client
from win32com.client import constants
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.utils import COMMASPACE
from speech2text import voiceIn

voiceOut = win32com.client.Dispatch("SAPI.spvoice")

def get_mail():
	uname = 'nileshfb9096@gmail.com'
	pawd = 'nilesh9096'
	unread_count = 0
	try:
		response = feedparser.parse('https://' + uname + ':' + pawd + '@mail.google.com/gmail/feed/atom')
		unread_count = response['feed']['fullcount']
		unreadable = 0
		if unread_count == 0:
			voiceOut.speak("You have no emails pending to be read.")
		else:
			voiceOut.speak("You have %d email unread in your account." %unread_count)
		for i in range(0, 10):
			try:
				print '(%s/%s) %s' %(str(i+1), str(10), response['items'][i].title)
				voiceOut.speak(response['items'][i].title)
				time.sleep(2)
			except Exception, err:
				unreadable += 1
		if unreadable > 0:
			voiceOut.speak('Sorry! Could not read %d emails.' %unreadable)

	except Exception, err:
		print str(err)
	return

def get_sub():
	voiceOut.speak('Speak out your subject.')
	sub = voiceIn()
	voiceOut.speak('Your response is %s.' %str(sub))
	return str(sub)

def send_email():
	try:
		server = smtplib.SMTP()
		server.connect('smtp.gmail.com', 587)
		print 'Connected to SMTP server.'
		server.ehlo()
		server.starttls()
		print 'Starting the TLS Connection with SMTP server...'
		server.login('nileshfb9096@gmail.com', 'nilesh9096')
		print 'Logged on to the SMTP server.'

		imap_host = 'imap.gmail.com'
		mail = imaplib.IMAP4_SSL(imap_host)
		#mail.login('nlieshfb9096@gmail.com', 'nilesh9096')

		msg = MIMEMultipart()
		msg['From'] = 'nileshfb9096@gmail.com'
		msg['To'] = 'nileshfbk123@gmail.com'
		msg['Subject'] = get_sub()
		msg.attach(MIMEText('\n\nHey this is Jarvis. Would you like to join in the project for audio assiatance. \n This is just part of it.'))
		msg.attach(MIMEText('\n\n\nMail sent by Jarvis.', 'plain'))
		server.sendmail('nilesh9096@gmail.com', 'ramesh_swami47@yahoo.co.in', msg.as_string())
		print 'Email was successfully sent.'
	except Exception, err:
		print str(err)

if __name__ == '__main__':
	send_email()
