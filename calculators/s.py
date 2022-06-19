from responsive_voice.voices import USEnglishMale
import os
import speech_recognition as sr


listener = sr.Recognizer()
engine = USEnglishMale()

def play(dir):
	engine.say(dir)
	if  "what is" in str(dir.lower()):
		pass
	if  "shut down" in dir:
		engine.say('have a good night sur',rate=0.44449)
		os.system('shutdown /s ')	


with sr.Microphone() as source:
	engine.say('dir')
	listener.adjust_for_ambient_noise(source, duration = 1)
	print('ready sir')
	voice = listener.listen(source)
	command =listener.recognize_google(voice)
	#print(command)
	play(command)
	engine.say(command)