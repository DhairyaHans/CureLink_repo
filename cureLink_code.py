# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:55:47 2022

@author: 91987
"""

import re
from datetime import datetime
import smtplib


class newsLetter():

	# Constructor
	def __init__(self):

		### Intialize the Current time and getting the time in the form of
		# "YY-MM-DD HH:MM:SS" (string)
		self.time = datetime.now()
		self.cTime = self.time.strftime("%Y-%m-%d %H:%M:%S")		
		
		### Initialize the dictionaries that store the data/info
		
		# __topics - store the topics available for the newsLetter with the time at which the last email was sent
		self.__topics = {"ai":self.cTime, "ml":self.cTime}
		
		# __subs - store the emails of the subscribers along with the topics to which they subscribed
		self.__subs = {"dummy@yahoo.com":"ai", "dummyemail@hotmail.com":"ml"}
		
		# __topic_specific_audience - store the list of subscribers of a particular topic
		self.__topic_specific_audience = {"ai":["dummy@yahoo.com"], "ml":["dummyemail@hotmail.com"]}
		
		# __topic_specific_content -  store the content of each topic, which is sent over the email to the subs
		self.__topic_specific_content = {"ai":[("Hello There", "I am AI Speaking"), "00:00:30"], 
								   "ml":[("HI Bro", "I am ML"), "00:01:00"]}
		
		
		print("Welcome to NewsLetter")
		
		### To Login using emailId
		self.login()
		
		
	### TO LOGIN USING EmailID
	def login(self):
		
		### Before each login, the emails will be sent, using the secheduleMails() function
		self.scheduleMails()
		
		### Logging In using emailId
		print("Enter Email address - ")
		self.emailId = input()
		
		# check_email_address() - checks the email to be in the right format
		if self.check_email_address(self.emailId):
			
			# validateEmail() - check whether the emailId belongs to the Admin or not
			# showContent() - shows the content to be shown to the user based on the post (Admin or Normal User)
			if self.validateEmail(self.emailId):
				print("Welcome Admin")
				# Admin - therefore flag = 1
				self.showContent(self.emailId, 1)
			else:
				print("Hello", self.emailId)
				# Normal User - therefore flag = 0
				self.showContent(self.emailId, 0)
				
		else:
			# Email is not in the right format
			print("Please re-enter the email")
			self.login()
		

	### TO CHECK THE FORMAT OF THE EmailID
	def check_email_address(self, emailId):
	  # Checks if the address match regular expression
	  is_valid = re.search('^\w+@\w+.\w+$', emailId)
	  # If there is a matching group
	  if is_valid:
	    return True
	  else:
	    print('It looks that provided mail is not in correct format. \n'
	          'Please make sure that you have "@" and "." in your address \n'
	          'and the length of your mail is at least 6 characters long')
	    return False


	### VALIDATE WHETHER THE LOGIN EmailID BELONGS TO ADMIN OR NOT
	def validateEmail(self, emailId):
		if emailId=="Your_admin_email_id@gmail.com":	# Enter your Admin's email ID
			return 1
		else:
			return 0


	
	### TO UPDATE CONTENT OF AN EXISTING TOPIC
	def updateContent(self, topic):
		print("Enter title of the content - ")
		self.title = input()
		print("Enter Content - ")
		self.content_text = input()
		print("Enter time interval to deliver the email (HH:MM:SS) - ")
		self.timeToDeliver = input()
		self.__topic_specific_content[topic] = [(self.title, self.content_text), self.timeToDeliver]


	### TO ADD A NEW TOPIC FOR NEWSLETTER
	def addNewTopic(self, new_topic):
		self.time = datetime.now()
		self.cTime = self.time.strftime("%Y-%m-%d %H:%M:%S")
		self.__topics[new_topic] = self.__topics.get(new_topic, self.cTime)
		self.updateContent(new_topic)
		
	
	### SHOW THE TOPICS AVAILABLE FOR NEWSLETTER
	def showTopics(self):
		if self.__topics == dict():
			print("Right now We don't have any specific topic")
			return 0
		else:
			print(*self.__topics.keys(), sep = "\n")
			return 1
		
		
	### SHOW THE LIST OF USERS ENROLLED/SUBSCRIBED FOR A PARTICULAR TOPIC
	def showUsers(self, topic):
		if topic in self.__topics:
			if self.__topic_specific_audience.get(topic, 0)==0:
				print("No one is enrolled till now")
			else:
				print(*self.__topic_specific_audience[topic], sep = "\n")
		else:
			print("Wrong Input")
					
			
	### TO SEND Email
	def sendMail(self, topic, timeToDeliver, title, content_text):
		self.smtp_server = "smtp.gmail.com"
		self.sender_email = "Your_admin_email_id@gmail.com" # Enter your sender email address
		self.receiver_email = self.__topic_specific_audience.get(topic, [])  # Enter receiver address
		self.password = "PASSWORD"    # Enter your sender email's password

		# To send email to all the subscribers		
		for dest in self.receiver_email:
			try: 
				self.message = 'Subject: {}\n\n{}'.format(title, content_text)


			    #Create your SMTP session 
				smtp = smtplib.SMTP('smtp.gmail.com', 587) 
			
			    #Use TLS to add security 
				smtp.starttls() 
			
			    #User Authentication 
				smtp.login(self.sender_email,self.password)
			
			    #Sending the Email
				smtp.sendmail(self.sender_email, dest,self.message) 
			
			    #Terminating the session 
				smtp.quit() 
				print ("Email sent successfully!") 
			
			except Exception as ex: 
			    print("Something went wrong....",ex)
		
	
	
	### TO ADD A NEW SUBSCRIBER TO A TOPIC 
	def newSubscriber(self, emailId, topic):
		self.__subs[emailId] = topic
		self.__topic_specific_audience.setdefault(topic, []).append(emailId)
		
	
	### TO CHANGE THE TOPIC OF SUBSCRIPTION FOR A PARTICULAR USER
	def changeSubsTopic(self, emailId, old_topic, new_topic):
		self.__topic_specific_audience[old_topic].remove(emailId)
		self.__subs[emailId] = new_topic
		self.__topic_specific_audience.setdefault(new_topic, []).append(emailId)
		
		
	### TO WITHDRAW SUBSCRIPTION
	def withdrawSubs(self, emailId, topic):
		del self.__subs[emailId]
		self.__topic_specific_audience[topic].remove(emailId)
	
	
	### TO GET SECONDS FROM TIME IN THE FORM(HH:MM:SS)
	def get_sec(self, time_str):
	    """Get seconds from time."""
	    h, m, s = time_str.split(':')
	    return int(h) * 3600 + int(m) * 60 + int(s)
	
	
	### TO SCHEDULE Emails BASED ON THE TIME INTERVAL GIVEN FOR EACH TOPIC
	def scheduleMails(self):
		for i in self.__topics.keys():
			
			# Get the last_sent time of a particular topic
			self.last_sent = datetime.strptime(self.__topics[i], "%Y-%m-%d %H:%M:%S")
			# Convert it into timestamp
			self.l_ts = self.last_sent.timestamp()
			
			
			# Get the current time 
			self.time = datetime.now()
			self.cTime = self.time.strftime("%Y-%m-%d %H:%M:%S")
			self.curTime = datetime.strptime(self.cTime, "%Y-%m-%d %H:%M:%S")
			# Convert it into timestamp
			self.c_ts = self.curTime.timestamp()
			
			# Get the Time interval after which Email is to be sent for a particular topic
			self.info = self.__topic_specific_content[i]
			self.title, self.content, self.timeToDeliver = self.info[0][0], self.info[0][1], self.info[1]
			# Convert the interval in (HH:MM:SS) to seconds
			self.interval = self.get_sec(self.timeToDeliver)
			
			# if current_time - last_sent_time > interval
			# then SendMail
			if self.c_ts-self.l_ts>=self.interval:
				self.sendMail(i, self.timeToDeliver, self.title, self.content)
				self.__topics[i] = self.cTime
			else:
				print("Already sent")
					
	
	### TO TAKE 'CHOICE' INPUT FROM USER
	def Input(self):
		try:
			ip = int(input())
			return ip
		except Exception:
			print("Enter the input again")
			return self.Input()
			
	
	### TO SHOW THE CONTENT TO USER BASED ON THE ROLE (ADMIN / NORMAL USER)
	def showContent(self, emailId, i):

		if i:
			print("What do you want to do...")
			print("1. Update content of a Specified topic")
			print("2. Add a new topic")
			print("3. See users(subscribers of a particular topic")
			print("4. Send a mail for a specific audience")
			print("5. To Login as a new user OR exit")
			print("Any other key to EXIT")
			
			self.ip = self.Input()
			print(self.ip)
			if self.ip==1:
				print("Choose from the following topics - ")
				print(*self.__topics, sep = "\n")
				print("Enter Topic whose content is to be changes - ")
				self.topic = input().lower()
				if self.topic in self.__topics:
					self.updateContent(self.topic)	
				else:
					print("Wrong choice")
				self.showContent(emailId, i)
			elif self.ip==2:
				print("Enter new Topic to be added - ")
				self.new_topic = input().lower()
				self.addNewTopic(self.new_topic)	
				self.showContent(emailId, i)
			elif self.ip==3:
				print("Available Topics - ")
				self.showTopics()
				print("Enter the topic for which u want to see users - ")
				self.topic = input().lower()
				self.showUsers(self.topic)
				self.showContent(emailId, i)
			elif self.ip==4:
				print("Enter the Topic of the spcific audience - ")
				self.topic = input().lower()
				print("Enter title of the maul - ")
				self.title = input()
				print("Enter Mail content - ")
				self.content_text = input()
				self.time = datetime.now()
				self.timeToDeliver = self.time.strftime("%H:%M:%S")
				if self.topic.lower()=="all":
					pass
				else:
					self.sendMail(self.topic, self.timeToDeliver, self.title, self.content_text)
				self.showContent(emailId, i)
			elif self.ip==5:
				print("Do u want to exit (Y/N) - ")
				self.x = input().upper()
				if self.x=='Y':
					return
				else:
					self.login()	
			else:
				print("BREAK")	
				return
			
		else:

			if self.__subs.get(emailId, 0)!=0:
				print("Seems like You are already a Subscriber of the topic ", self.__subs[emailId])
				print("We have 2 options for you - ")
				print("1. Change the topic of subscription")
				print("2. Withdraw Subscription")	
				print("3. To Login as a new user OR exit")
				print("Any other key to EXIT")
				print("Choose - ")
				self.ip = self.Input()
				if self.ip==1:		
					print("Our Topics List - ")
					print(*self.__topics.keys(), sep = "\n")
					print("Enter the topic you want to subscribe now - ")
					self.new_topic = input().lower()
					self.changeSubsTopic(emailId,self.__subs[emailId], self.new_topic)
					self.showContent(emailId, i)
				elif self.ip==2:
					self.withdrawSubs(emailId,self. __subs[emailId])
					self.showContent(emailId, i)
				elif self.ip==3:
					print("Do u want to exit (Y/N) - ")
					self.x = input().upper()
					if self.x=='Y':
						return
					else:
						self.login()	
				else:
					print("BREAK")
					return
			else:
				print("Welcome new user")
				print("We are delighted to have you")
				print("Do you want to subscribe to a channel(Y/N) - ")
				self.x = input()
				if self.x.upper()=='Y':
					print("We have a number of topics from which you can subscribe to one -")
					
					if self.showTopics():
						print("Enter the topic you want to subscribe to - ", end="\n\n")
						self.topic = input().lower()
						self.newSubscriber(emailId, self.topic)
						print("Do u want to exit (Y/N) - ")
						self.x = input().upper()
						if self.x=='Y':
							return
						else:
							self.showContent(emailId, i)
					else:
						print("Do u want to exit (Y/N) - ")
						self.x = input().upper()
						if self.x=='Y':
							return
						else:
							self.login()
				else:
					print("Do u want to exit (Y/N) - ")
					self.x = input().upper()
					if self.x=='Y':
						return
					else:
						self.login()			
				
if __name__=="__main__":
	newsL = newsLetter()
	
	
	
	
	
	
	
	
				
				
				
		
	

		




