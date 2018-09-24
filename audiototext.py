import urllib
import speech_recognition as sr
import subprocess
import os



cmdline = ['avconv',
           '-i',
           'test.mp3',
           '-vn',
           '-f',
           'wav',
           'test.wav']
subprocess.call(cmdline)

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

command = r.recognize_google(audio)
print(command)

#os.remove("test.mp3")
os.remove("test.wav")