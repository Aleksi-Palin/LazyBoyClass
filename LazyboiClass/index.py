import json
from datetime import datetime,date
import speech_recognition as sr

r = sr.Recognizer()

run = True

data = {}

with open("notepad.json", "r") as file:
    data = json.load(file)


while run:
    with sr.Microphone() as source:
        
        try:
            print("Listening...")
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text, language="fi-FI")
            
            #print("Done listening...")

            now = datetime.now()
            timestamp = date.today()

            current_time = now.strftime("%H:%m")

            data["notes"].append({
                str(timestamp) +" - "+ current_time : text
            })
            
            with open("notepad.json", "w") as file:
                file.write(json.dumps(data,indent=4))
                print("New Note added")

        except KeyboardInterrupt:
            print("Stopping")
        except:
            print("Error")
            run = False