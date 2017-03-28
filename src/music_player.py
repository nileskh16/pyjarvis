import os, random, mp3play, time
from math import floor
from mutagen.mp3 import MP3

def mp3files():
	mp3list = []
	try:
		basedir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
		mp3_source = os.path.join(basedir, 'data_files', 'mp3_files')
		for paths, dirs, files in os.walk(mp3_source):
			for file in files:
				if file.endswith('.mp3'):
					mp3list.append(os.path.join(paths, file))
					#print os.path.join(paths, file)

	except Exception, err:
		print str(err)
		pass

	return mp3list

def mlength(mfile):
	audio = MP3(mfile)
	return audio.info.length

def play_music():
	mp3list = mp3files()
	for i in random.sample(mp3list, len(mp3list)):
		print i
		clip = mp3play.load(i)
		clip.play()
		fileln = mlength(i)
		secs = clip.seconds()
		print '%d:%d' %(secs/60, secs%60)
		#time.sleep(min(fileln, clip.seconds()))
		time.sleep(30)
		clip.stop()

if __name__ == '__main__':
	play_music()
