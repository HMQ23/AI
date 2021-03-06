import speech_recognition
import pyttsx3
from datetime import date, datetime
import wikipedia, webbrowser
import requests, json

AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
AI_brain = ""

def there_exists(terms):
    for term in terms:
        if term in you:
            return True

x = datetime.now()
timenow = int(x.strftime("%H"))
if 5 < timenow < 12 :
    print("Good Morning")
elif 12 <= timenow < 13 :
    print("Lunch time")
elif 13 <= timenow < 18 :
    print("Good Afternoon")
elif 18 <= timenow < 23 :
    print("Good Evening")
elif timenow >= 23 or 0 <= timenow <= 5:
    print("Time to sleep now!")

while True:
    rate = AI_mouth.getProperty('rate')
    AI_mouth.setProperty('rate', 150)

    voices = AI_mouth.getProperty('voices')
    AI_mouth.setProperty('voice', voices[1].id)

    with speech_recognition.Microphone() as mic:
        AI_ear.adjust_for_ambient_noise(mic) 
        print("AI: I'm Listening")
        audio = AI_ear.record(mic, duration=5)

    print("AI: ...")

    try:
        you = AI_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if "hello" in you:
        AI_brain = "hi, what can I help you"
    elif there_exists(["how are you","how are you doing"]):
        AI_brain = "I'm very well, thanks for asking me"
    elif there_exists(["what's the date today","what is the date today","tell me about the date today","what day is today"]):
        todays = date.today()
        AI_brain = todays.strftime("Today is %B %d, %Y.")
    elif "time" in you:
        times = datetime.now()
        AI_brain = times.strftime("It's %H hours and %M minutes.")
    elif "Wikipedia" in you or "wiki" in you: 
        AI_brain = "This is Wikipedia"
        print("AI: " + AI_brain)
        AI_mouth.say(AI_brain)
        AI_mouth.runAndWait()
        while True:
            AI_brain = "Please state what you want to search or exit"
            print("Wikipedia: " + AI_brain)
            AI_mouth.say(AI_brain)
            AI_mouth.runAndWait()
            hear = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as mic:
				
                wikiinput = hear.listen(mic)
                try:					
                    wiki = hear.recognize_google(wikiinput)
                    print("Wikipedia: ...")
                    print("You: " + wiki)
                    if wiki == "end" or wiki == "exit" or wiki == "out":
                        break
                    else:
                        try:
                            searchresult = wikipedia.summary(wiki, sentences=2, auto_suggest=True, redirect=True)
                        except:
                            searchresult = "Can't find"
							
                        print("Wikipedia: " + searchresult)
                        AI_mouth.say(searchresult)
                        AI_mouth.runAndWait()
						
                except:
                    print("Wikipedia: I can't get it")
                    AI_mouth.say("I can't get it")
                    AI_mouth.runAndWait()
        AI_brain = "End of Wikipedia search"
    elif there_exists(["open Google","search Google"]):
        search_term = you.split("google")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        AI_brain = "Here is what I found for" + search_term + " on google."
    elif there_exists(["YouTube"]):
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        AI_brain = "Done!"
    elif there_exists(["weather"]):
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        AI_brain = "Here is the weather today."
    elif you == "":
        AI_brain = "Sorry I don't understand what you say"
    elif there_exists(["exit", "quit", "goodbye", "bye", "catch you later", "see you later", "see you soon", "talk to you later"]):
        AI_brain = "It was great to meet you. See you later!"
        print("AI: " + AI_brain)
        AI_mouth.say(AI_brain)
        AI_mouth.runAndWait()
        exit()
    else:
        AI_brain = "Sorry, I don't understand what you're saying!"

    print("AI: " + AI_brain)
    AI_mouth.say(AI_brain)
    AI_mouth.runAndWait()
