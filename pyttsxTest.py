import sounddevice as sd
import pyttsx3
import numpy as np
import wave
import os
import sys
import signal
import inspirobot
#get devices list
devices = sd.query_devices()
# print(devices)

#set output device to 6
# sd.default.device = 6
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
#print the voices
voices = pyttsx3.init().getProperty('voices')
for voice in voices:
    print(voice)
    # if "Haruka" in voice.name:
    # # if "David" in voice.name:
    #     engine.setProperty('voice', voice.id)
    #     break


#setup pyttsx3

engine.say('Hello World')
engine.runAndWait()

# def signal_handler(signal, frame):
#     print("halting")
#     #if sd is playing, stop it
#     if sd.get_status() == sd.Status.RUNNING:
#         sd.stop()
#     else:
#         sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)



text = None

channels = {5}
while text != 'exit':
    text = input('Say something: ')
    #if .text.wav exists, delete it
    try:
        os.remove('.test.wav')
    except:
        pass
    if "--voice" in text:
        for voice in voices:
            print(voice)
            if text.split()[1] in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        continue
    elif "--volume" in text:
        engine.setProperty('volume', float(text.split()[1]))
        continue
    elif "--rate" in text:
        engine.setProperty('rate', float(text.split()[1]))
        continue
    elif "--device" in text:
        d = int(text.split()[1])
        # if d in channels:
        #     channels.remove(d)
        # else:
        #     channels.add(d)
        sd.default.device = d
        continue
    elif "--inspire" in text:
        text = inspirobot.getQuote()
        print(text)
        if (input("Send?") == 'n'):
            continue
    elif "--" in text:
        continue
    engine.save_to_file(text, '.test.wav')
    engine.runAndWait()
    #read wav file
    wf = wave.open('.test.wav', 'rb')
    data = wf.readframes(-1)
    data = np.frombuffer(data, dtype=np.int16)
    fr = wf.getframerate()
    wf.close()
    #play wav file
    sd.play(data, fr)
    sd.wait()
    sd.stop()
    #non-blocking
    # sd.play(data, fr, callback=sd_callback)


