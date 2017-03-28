import os, sys, random, win32com.client, re

from src.dark import dark_light
from src.dev import machine_info, get_time, is_internet
from src.music_player import play_music
from src.send_email import send_email
from src.speech2text import voiceIn
from src.wav import wav_play
from src.misc import get_wiki, make_call, take_screenshot
from win32com.client import constants

voiceOut = win32com.client.Dispatch('SAPI.spvoice')

def run_jarvis():
    wav_play()
    voiceOut.speak('Hello Everyone! This is Jarvis. U may call me Tinker. I\'m here to help you all through your tough times.')
    voiceOut.speak('Just tell me what\'s on your mind now?')

    while True:
        voice = voiceIn()
        voiceOut.speak('Recongnizing it....')
        if voice == None:
            voiceOut.speak('Ohhh! Sorry! Could not hear you. Possibly the Microphone is not working. Try again later.')
            sys.exit(0)
        elif bool(re.search(r'\bJarvis|Tinker\b', voice, re.IGNORECASE)):
            voiceOut.speak('Hey! Yes. I could hear you. Tell me.')
        elif bool(re.search(r'\bmusic|song|audio|track|play|listen\b', voice, re.IGNORECASE)):
            voiceOut.speak('Ok! Playing songs for you. Enjoy.')
            play_music()
        elif bool(re.search(r'\bsend|email|gmail|outbox|send an email\b', voice, re.IGNORECASE)):
            voiceOut.speak('Ok Now sendiang an email to ramesh_swami47@yahoo.co.in')
            send_email()
        elif bool(re.search(r'\bdark|outside\b', voice, re.IGNORECASE)):
            voiceOut.speak('OK. Now sneaking out to check the light.')
            msg = "Don't even step out of your house. It's dark outside." if dark_light() else "Yes u can go outside and do whatever you want because it is not dark yet."
            voiceOut.speak(msg)
        elif bool(re.search(r'\btime now|clock|time\b', voice, re.IGNORECASE)):
            voiceOut.speak('Checking the clock for you.')
            curtime = 'And it is %s on clock.' %get_time()
            voiceOut.speak(curtime)
        elif bool(re.search(r'\binternet|is connected|online\b', voice, re.IGNORECASE)):
            voiceOut.speak('Now checking the internet connection.')
            status = 'Yes. U are now linked to the outside world.' if is_internet() else 'Unfortunately. U have to plug the LAN cable in.'
            voiceOut.speak(status)
        elif bool(re.search(r'\bFacebook|fb|face book|messanger\b', voice, re.IGNORECASE)):
            os.startfile('https://www.facebook.com')
        elif bool(re.search(r'\bgoogle|search online\b', voice, re.IGNORECASE)):
            os.startfile('https://www.google.co.in')
        elif bool(re.search(r'\bwikipedia|information|wiki\b', voice, re.IGNORECASE)):
            voiceOut.speak('What do you want to search about?')
            article_title = voiceIn()
            result = get_wiki(article_title)
            print "\n%s" %str(result)
        elif bool(re.search(r'\bscreenshot|desktop\b', voice, re.IGNORECASE)):
            take_screenshot()
            voiceOut.speak('Taking the screenshot now...')
        elif bool(re.search(r'\bgoodbye|bye|sleep now|rest|done|exit now|stop it|stop|close', voice, re.IGNORECASE)):
            voiceOut.speak('Ok! Time to hibernate now but not forever. Just call me when you will need me. Bye! Bye! Hope U will be fine. C u soon.')
            sys.exit(0)
        else:
            voiceOut.speak('Ohhh. Sorry! Could not identify your command. Would you please like to try again?')

if __name__ == '__main__':
    run_jarvis()
