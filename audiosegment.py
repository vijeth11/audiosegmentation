import json;
import os
import speech_recognition as sr
from pyAudioAnalysis import audioTrainTest as aT

def traindata(subdirectories):
	print(subdirectories)
	aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)
	listoffiles=[]
	speech=[]
	speakerName={}
	index=0
	r = sr.Recognizer()
	for i in subdirectories:
	    listoffiles.append(os.listdir(i))
	    gotName=False
	    k=0
	    while not gotName:
	        try:
	           data=aT.fileClassification(i+"/"+listoffiles[index][k], "svmModel","svm")
	           speakerName[i]=data[2][data[1].tolist().index(max(data[1]))]
	           index+=1
	           gotName=True
	        except:
	            k+=1
	            continue
	    print(speakerName)
	    for i in range(0,len(subdirectories)):
	        for j in listoffiles[i]:
	            audiofile = sr.AudioFile(subdirectories[i]+"/"+j)
	            with audiofile as source:
	                r.adjust_for_ambient_noise(source,duration=0.05)
	                audio = r.record(source)
	            print("audio file"+j)
	            try:
	                print("User: " + r.recognize_google(audio))
	                speech.append({speakerName[subdirectories[i]]:r.recognize_google(audio)})
	            except sr.UnknownValueError:
	                print("Google Speech Recognition could not understand audio")
	            except sr.RequestError as e:
	                print("Could not request results from Google Speech  Recognition service; {0}".format(e))
	print(speech)
	return speech

def segment():
	with open('English_lesson.json') as data_file:
     		json_data = data_file.read()
	data = json.loads(json_data)
	speakers=data["results"]["speaker_labels"]["segments"]
	count=0
	subdirectories = []
	for i in speakers:
	    print(i["speaker_label"])
	    print(i["start_time"])
	    print(i["end_time"])
	    try:
	        if(not os.path.exists(i["speaker_label"])):
	            os.makedirs(i["speaker_label"])
	            print("dir is not present making")
	            subdirectories.append(i["speaker_label"])
	        os.system("avconv -i English_audio_4.wav -ss "+i["start_time"]+" -to "+i["end_time"]+" -acodec copy "+i["speaker_label"]+"/output"+str(count)+".wav");
	        count+=1
	    except OSError as e:
	        print("exception found"+e.getmessage())
	return subdirectories

#traindata(segment());
#traindata([u'spk_1', u'spk_0'])

#with open('transcribingoutput15.json') as data_file:
#     		json_data = data_file.read()
#data = json.loads(json_data)
#print(data["results"]["transcripts"][0]["transcript"])


