#####	This is the code for Curelink Intern Assignment for Backend Developer	#####

#####	Problem statement: Newsletter Service

You are expected to make an app or a service which will send pre-decided content to a specific set of users[subscriber] at specified intervals/time. 

#####	Goals:
	
1. A system to enter subscriber’s email ids. 
2. A system to enter content, with time & content text. 
3. Content should be segregated on topic basis. There can be multiple topics and content will belong to a specific topic. 
4. Each user will subscribe to a specific topic. 

##### PREREQUISITES - 
	
	### LANGUAGE USED - 
		
		Python 3.8.8

	### MODULES - 
		1. re		(pip install regex)	# To check the format of emailID
		2. datetime	(pip install datetime2)	
		3. smtplib	(pip install secure-smtplib)	# For Mail Transfer


##### CODE OVERVIEW - 

	The Code contains one class - "newsLetter"

	### VARIABLES - 
	
	1. __topics : 
		
		- Dictionary (dict())
		- store the topics available for the newsLetter with the time at which the last email was sent
	
	2. __subs :
		
		- Dictionary (dict())
		- store the emails of the subscribers along with the topics to which they subscribed	

	3. __topic_specific_audience :

   		- Dictionary (dict())
		- store the list of subscribers of a particular topic

	4. __topic_specific_content :

		- Dictionary (dict())
		- store the content of each topic, which is sent over the email to the subs

	### Functions -
	
	1. __init__ :
			
		- Arguments -> NONE
		- Constructor
		- Initialize the Current time and getting the time in the form of "YY-MM-DD HH:MM:SS" (string)
		- Initialize the dictionaries that store the data/info
		- Calls the login() function to login user

	2. login() : 

		- Arguments -> NONE
		- To Login Using EmailId
		- Before each login attempt, it Calls the 'scheduleMails()' function to send the pending NewsLetter mails
		- After Inputting the emailId, it Check the format of the emailId, by calling 'check_email_address()' function
		- If the emailId format is right, It then calls the 'validateEmail()' function to check whether the emailId belongs
			to Admin (set by user) or not
		- And then it calls the 'showContent()' function to show the content of the program to the user based on the
			role(Admin / Normal User)

	3. check_email_address():
  
		- Arguments ->
			<> emailId : String type, emailId inputted by the user
		- To Check the format of the emailId
		- Return Type - Boolean(True/False)
		
	4. validateEmail():
	
		- Arguments ->
			<> emailId : String type, emailId inputted by the user
		- Validate whether the emailId belongs to the Admin or not
		- Admin emailId is already given by the user (assumption) 
		- Return Type - Boolean(True/False)
		
	5. updateContent():
		
		- Arguments ->
			<> topic : String type, Topic of the newsletter domain, whose content is to be changed
		- To Update the Content of an Existing Topic
		- Returns Nothing

	6. addNewTopic():
		
		- Arguments ->
			<> new_topic : String type, New_topic which is to be added by the Admin
		- To add a new topic for newsLetter
		- Returns Nothing

	7. showTopics():
		
		- Arguments -> NONE
		- To show the list of available topics for newsLetter
		- Return type - (0/1)

	8. showUsers():

		- Arguments ->
			<> topic : String type, Topic of the newsletter domain, whose subscribers are to be listed
		- Show the list of the users enrolled/subscribed for a particular topic
		- Returns Nothing

	9. sendMail():

		- Arguments ->
			<> topic : String type, Topic of the newsletter domain, whose audience will recieve the Email
			<> timeToDeliver : String (HH:MM:SS), Time Interval After which Email will be sent
			<> title : String, Title/Subject of the Email
			<> content_text : String, Content/Body of the Email
		- To send Email
		- Uses SMTP to send Email
		- EmailId and Password of the Sender's email is already stored here
		- If "login Credentials not working" ERROR occurs, check the link 
			https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
		- Returns Nothing

	10. newSubscriber():

		- Arguments ->
			<> emailId : String type, EmailId of the user
			<> topic : String type, Topic of the newsletter domain, to which the user wants to subscribe
		- To Add a new subscriber to a topic
		- Returns Nothing

	11. changeSubsTopic():

		- Arguments ->
			<> emailId : String type, EmailId of the user
			<> old_topic : String type, Old Topic of the newsletter domain, to which the user was subscribed
			<> new_topic : String type, New Topic of the newsletter domain, to which the user wants to subscribe
		- To Change the topic of Subscription for a particular user
		- Returns Nothing

	12. withdrawSubs():
		
		- Arguments ->
			<> emailId : String type, EmailId of the user
			<> topic : String type, Topic of the newsletter domain, from which the user wants to withdraw subscription
		- To withdraw Subscription
		- Returns Nothing

	13. get_sec():

		- Arguments ->
			<> time_str : String (HH:MM:SS), time_interval to send mail
		- To get seconds from time in the form (HH:MM:SS)
		- Returns Nothing

	14. scheduleMails():

		- Arguments -> NONE
		- To Schedule Emails based on the time interval given for each topic
		- Returns Nothing

	15. Input():
		
	 	- Arguments -> NONE
		- To take "CHOICE" input from user
		- Returns integer ("Choice of the user")

	16. showContent():
	
		- Arguments ->
			<> emailId : String type, EmailId of the user
			<> i : int type, 1 : if the user is Admin, 0 : Otherwise
		- To show the content of the program to the user based on the role(Admin / Normal User)
		- Returns Nothing



		

		

			
		
					
		



