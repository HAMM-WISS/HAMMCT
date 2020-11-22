import amino
import os

green = "\033[0;32m"
red = "\033[0;31m"
white = "\033[0;37m"
black = "\033[0;30m"
ON_blue="\033[44m"
ON_green="\033[42m"
ON_black="\033[40m"
os.system("clear")
print("  __   __     _____     __      __    __      __") 
print("/|::|/|::|  //:::::\  /|::\    /::| /|::\    /::|") 
print("||::|||::| //::/\\\::\ ||:::\  /:::| ||:::\  /:::|") 
print("||::|||::| ||::|||::| ||::::\/::::| ||::::\/::::|") 
print("||:::::::| ||:::::::| ||::|\::/|::| ||::|\::/|::|") 
print("||::|||::| ||::|||::| ||::|/_/||::| ||::|/_/||::|") 
print("||::|||::| ||::|||::| ||::|   ||::| ||::|   ||::|") 
print("||::|||::| ||::|||::| ||::|   ||::| ||::|   ||::|") 
print("|/__/|/__/ |/__/|/__/ |/__/   |/__/ |/__/   |/__/") 

print(green + "------------------------------------------------"+white)
client=amino.Client()
sms=True
if sms ==True:
	try:
		email=input(green+"ENTER YOUR EMAIL :  "+white)
		password=input(green+"ENTER YOUR PASSWORD :  "+white)
		client.login(email=email,password=password)
	except:
		choice=input(red+"Incorrect Email or password! Do u want to retry?(Y/N) :  "+white)
		if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes" or choice == "":
			try:
				email=input(green+"ENTER YOUR EMAIL :  "+white)
				password=input(green+"ENTER YOUR PASSWORD :  "+white)
				client.login(email=email,password=password)
			except:
				print(red+"2 Incorrect sign in(s) = exit:)")
				os._exit(1)
		if choice == "N" or choice == "n" or choice == "No" or choice == "no":
			os._exit(1)
			try:
				email=input(green+"ENTER YOUR EMAIL :  "+white)
				password=input(green+"ENTER YOUR PASSWORD :  "+white)
				client.login(email=email,password=password)
			except:
				print(red+"2 Incorrect sign in(s) = exit:)")
				os._exit(1)
		if choice == "N" or choice == "n" or choice == "No" or choice == "no":
			os._exit(1)

greek="greek"
if greek=="greek":
	try:
		curl=input("CHAT URL : ")
		courl=client.get_from_code(curl)
		chatId=courl.objectId
		comId=courl.path[1:courl.path.index('/')]
		subclient=amino.SubClient(comId=comId,profile=client.profile)
		subclient.join_chat(chatId=chatId)
	except:
		print(red+"Invalid URL"+white)
		choice = input("Do u want to retry?(Y/N) :  ")
		if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes" or choice == "":
			try:
				curl=input("CHAT URL : ")
				courl=client.get_from_code(curl)
				chatId=courl.objectId
				comId=courl.path[1:courl.path.index('/')]
				subclient=amino.SubClient(comId=comId,profile=client.profile)
				subclient.join_chat(chatId=chatId)
			except:
				print(red+"2 invalid URL(s) = exit:)"+white)
				os._exit(1)
		if choice == "N" or choice == "n" or choice == "No" or choice == "no":
			os._exit(1)
os.system("clear")
five =5
if 5 != 10:
	message=input("ENTER THE MESSAGE :  ")
	messtype=input("MESSAGE TYPE (0/1/55/110) :  ") 	
	while True: 		
		try: 			
			subclient.send_message(message=message,messageType=messtype,chatId=chatId)
			print(green+"Message sent:)")
		except: 			
			print(green+"Message sent:)")
