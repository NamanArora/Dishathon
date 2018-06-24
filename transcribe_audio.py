import speech_recognition as sr

r = sr.Recognizer()

audio = '/home/naman/Desktop/SpeechRecognition-master/speech1.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)
    f = open("speech.txt","w")
    f.write(text)
    
except Exception as e:
    print (e)
