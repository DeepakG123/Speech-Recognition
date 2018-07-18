import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

#Test to see if the record method is properly storing the data in 'audio'
print(type(audio))

#Transcribes audio file
print(r.recognize_google(audio))

#------------------------------Capture only part of an audio file---------------------------------------------
#Trascibe first 4 seconds
with harvard as source:
    audio = r.record(source, duration =4)



