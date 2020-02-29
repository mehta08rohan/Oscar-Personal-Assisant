import speech_recognition as sr 
import pyttsx3
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()	
available_microphone = sr.Microphone.list_microphone_names()

def listen():
	try:
		with sr.Microphone() as source:
			r.pause_threshold = 0.8
			my_audio = r.listen(source)
			my_text = r.recognize_google(my_audio)
			print("You Said :", my_text)
	except sr.RequestError as e: 
	        print("Could not request results; {0}".format(e)) 
	except sr.UnknownValueError: 
		print("unknown error occured")
	return my_text

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def openUrl(url):
	# chrome_options = Options()
	# chrome_options.add_experimental_option("detach", True)
	global broswer

	broswer = webdriver.Chrome('C:\\Users\\rohan.mehta\\Desktop\\SublimeText\\Oscar\\chromedriver.exe')
	broswer.get(url)

def pick_a_joke():
	jokes = ["Girl : What is the best thing about Switzerland? Boy : I don’t know, but the flag is a big plus.","Did you hear about the claustrophobic astronaut? ... He just needed a little space.","Why do not scientists trust atoms? ... Because they make up everything.","Where are average things manufactured? ... The satisfactory.","A man tells his doctor, Doc, help me. I am addicted to Twitter! The doctor replies Sorry, I don’t follow you…","Why do not Calculus majors throw house parties? ... Because you should never drink and derive.","What is the different between a cat and a comma? ... A cat has claws at the end of paws; A comma is a pause at the end of a clause."]
	return random.choices(jokes)

# def open_top_claim():
# 	claimurl = r"http://localhost/ADCC11_AFS.Claims/Desktop/HomePage/Default.aspx?src=%2fADCC11_AFS.Claims%2fDesktop%2fHomePage%2fHomePage.aspx&StaticPulseMode=true&IframeMode=true&UserStateId=08D769B31D0C5A82"
# 	global my_broswer
# 	my_broswer = webdriver.Chrome('C:\\Users\\rohan.mehta\\Desktop\\SublimeText\\Oscar\\chromedriver.exe')
# 	my_broswer.get(claimurl) 
# 	print(my_broswer.page_source)




if __name__ =="__main__":

	speak('Hi Rohan! What do you want me to do')
	
	while True:
		print('Listening. . . ')
		commands = listen()
		# print(commands)
		
		if "open" and "claim" and "application" in commands.lower():
			speak('Opening Your Claim Application')
			openUrl(r"http://localhost/ADCC11_AFS.Claims/Desktop/HomePage/Default.aspx?src=%2fADCC11_AFS.Claims%2fDesktop%2fHomePage%2fHomePage.aspx&StaticPulseMode=true&IframeMode=true&UserStateId=08D769B31D0C5A82")


		elif ("laugh" in commands.lower()) or ("joke" in commands.lower()) or ("jokes" in commands.lower()):
			speak("let me share a joke with you.")
			joke_selected =pick_a_joke()
			speak(joke_selected)
			

		elif ("quit" in commands.lower()) or ("thank you" in commands.lower()):
			speak("Your Welcome! Bye")
			break
		
		elif "your name" in commands.lower():
			speak("My name is Oscar")

		elif "the time" in commands.lower():
			time = datetime.datetime.now().strftime("%H:%M")
			speak(f"Its {time}.")

		elif "open top claim":
			speak("This Feature would be come in Version 2 of me.")

		else:
			speak('I am afraid , I cannot do that.')












	



