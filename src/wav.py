import os, time, re, wave, pyaudio, sys

CHUNK = 1024

base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
wav_source = os.path.join(base_dir, 'data_files', 'beep_hi.wav')

def wav_play():
        wf = wave.open(wav_source, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )
        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    wav_play()
