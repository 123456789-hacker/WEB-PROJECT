import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",  400)

rate = engine.getProperty("rate")
print(rate)


engine.say("Cześć Alan")

engine.runAndWait()

print(engine.getProperty("rate"))

#voices = engine.getProperty("voices")
#for voice in voices:
      #print("Voice " + voice.name )
      #print("Voice ID " + voice.id)
      #print("Voice Languages " + str(voice.languages))
      #print("Gender: "  + str(voice.gender))
      #print("Age:) " + str(voice.age))
      #print("\n")

