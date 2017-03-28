import os, time, win32com.client, json
from win32com.client import constants
from urllib2 import Request, urlopen, URLError
from twilio.rest import TwilioRestClient

voiceOut = win32com.client.Dispatch('SAPI.spvoice')

def take_screenshot():
    base_dir = os.path.dirname(os.path.dirname(os.path.absname(__file__)))
    img_path = os.path.join(base_dir, 'data_files\screenshots')
    img_name = '{0}_{1}.{2}'.format('screenshot', time.strftime('%d%m%y_%I%M%S'), 'jpg')
    im1 = pyautogui.screenshot(img_path, img_name)
    voiceOut.speak("The screenshot has been successfully taken.")
    return

def make_call():
    accountsid = '#####'
    authtoken = '#####'
    client = TwilioRestClient(accountsid, authtoken)
    '''call = client.calls.create(to = ,
        from = ,
        url = 'http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient')
    return call.sid'''

def get_wiki(article_title):
    print article_title
    request = Request('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+article_title)
    try:
        result = urlopen(request)
        response = json.load(result)
        output = response["query"]["pages"]
        final = output[output.keys()[0]]["extract"]
        print final
        return final
    except URLError, e:
        print str(e)
        return str(e)

if __name__ == '__main__':
    get_wiki(raw_input("Enter the search term: "))
