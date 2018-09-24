from googlesearch import *
from time import ctime
import nltk
#from gtts import gTTS
import os
from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("punkt")

def tokenizing(data):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    if len(filtered_sentence)==0:
       return data
    else:
       return filtered_sentence

def jarvis(data):
    print("tokenized result")
    print(tokenizing(data))
    if "how are you" in data:
        #speak("I am fine")
        return "I am fine"
    if "what" in data and "time" in data:
        #speak(ctime())
        return ctime()
    if "who created you" in data:
        #speak("I was born at Fri Aug 10 13:23:57 2018. My creater is Vijeth.")
        return "I was born at Fri Aug 10 13:23:57 2018. My creater is Vijeth."
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        #speak("Hold on Vijeth, I will show you where " + location + " is.")
        os.system("firefox https://www.google.nl/maps/place/" + location )
    if "how to reach" in data:
        data= data.split(" ")
        location =[data[3],data[4]]
        #speak("Hold on Vijeth, I will get you the direction ")
        os.system("firefox  https://www.google.nl/maps/dir/"+location[0]+"/"+location[1])
    else:
        result=search(data)
        #speak("hi Vijeth this is what i found")
        #speak(result)
        return "hi Vijeth this is what i found"+"\n"+result



#speak("Hello I am Jarvis your AI asistant")
#time.sleep(2)
#speak("Hi Vijeth, what can I do for you?")
#while 1:
    #data = recordAudio()
    #data = input()
    #jarvis(data)
