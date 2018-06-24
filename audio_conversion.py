from gtts import gTTS
mytext=open('output.txt','r')
mytext1=mytext.read()
mytext2=mytext1.decode('utf-8')
language='hi'
myobj=gTTS(text=mytext2,lang=language,slow=False)
myobj.save('converted_speech.mp3')
