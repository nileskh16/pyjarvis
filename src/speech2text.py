import speech_recognition as sr
import win32com.client
from win32com.client import constants

voiceout = win32com.client.Dispatch('SAPI.spvoice')

def voiceIn():
	try:
		r = sr.Recognizer()
		resp = ''
		with sr.Microphone() as source:
			#print r.energy_threshold
			r.adjust_for_ambient_noise(source, duration = 2)
			voiceout.speak("Now speak into the microphone.")
			audio = r.listen(source)
			try:
				resp = r.recognize_google(audio)
				print resp
			except Exception, err:
				voiceout.speak("Could not recognize the voice.")
		return resp
	except Exception, err:
		print str(err)
		
if __name__ == "__main__":
	voiceIn()