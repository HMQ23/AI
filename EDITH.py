import speech_recognition
import pyttsx3
from datetime import date, datetime
import wikipedia, webbrowser
import requests, json

EDITH_ear = speech_recognition.Recognizer()
EDITH_mouth = pyttsx3.init()
EDITH_brain = ""

def there_exists(terms):
    for term in terms:
        if term in you:
            return True

x = datetime.now()
timenow = int(x.strftime("%H"))
if 5 < timenow < 12 :
    EDITH_brain = "Good Morning"
elif 12 <= timenow < 13 :
    EDITH_brain = "Lunch time"
elif 13 <= timenow < 18 :
    EDITH_brain = "Good Afternoon"
elif 18 <= timenow < 23 :
    EDITH_brain = "Good Evening"
elif timenow >= 23 or 0 <= timenow <= 5:
    EDITH_brain = "Time to sleep now!"

while True:
    rate = EDITH_mouth.getProperty('rate')
    EDITH_mouth.setProperty('rate', 150)

    voices = EDITH_mouth.getProperty('voices')
    EDITH_mouth.setProperty('voice', voices[1].id)

    with speech_recognition.Microphone() as mic:
        EDITH_ear.adjust_for_ambient_noise(mic) 
        print("EDITH: I'm Listening")
        audio = EDITH_ear.record(mic, duration=5)

    print("EDITH: ...")

    try:
        you = EDITH_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if "hello" in you:
        EDITH_brain = "hi, what can I help you"
    elif there_exists(["how are you","how are you doing"]):
        EDITH_brain = "I'm very well, thanks for asking me"
    elif there_exists(["what's the date today","what is the date today","tell me about the date today","what day is today"]):
        todays = date.today()
        EDITH_brain = todays.strftime("Today is %B %d, %Y.")
    elif "time" in you:
        times = datetime.now()
        EDITH_brain = times.strftime("It's %H hours and %M minutes.")
    elif "Wikipedia" in you or "wiki" in you: 
        EDITH_brain = "This is Wikipedia"
        print("EDITH: " + EDITH_brain)
        EDITH_mouth.say(EDITH_brain)
        EDITH_mouth.runAndWait()
        while True:
            EDITH_brain = "Please state what you want to search or exit"
            print("Wikipedia: " + EDITH_brain)
            EDITH_mouth.say(EDITH_brain)
            EDITH_mouth.runAndWait()
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
                        EDITH_mouth.say(searchresult)
                        EDITH_mouth.runAndWait()
						
                except:
                    print("Wikipedia: I can't get it")
                    EDITH_mouth.say("I can't get it")
                    EDITH_mouth.runAndWait()
        EDITH_brain = "End of Wikipedia search"
    elif there_exists(["open Google","search Google"]):
        search_term = you.split("google")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        EDITH_brain = "Here is what I found for" + search_term + " on google."
    elif there_exists(["YouTube"]):
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        EDITH_brain = "Done!"
    elif there_exists(["weather"]):
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        EDITH_brain = "Here is the weather today."
    elif you == "":
        EDITH_brain = "Sorry I don't understand what you say"
    elif there_exists(["exit", "quit", "goodbye", "bye", "catch you later", "see you later", "see you soon", "talk to you later"]):
        EDITH_brain = "It was great to meet you. See you later!"
        print("EDITH: " + EDITH_brain)
        EDITH_mouth.say(EDITH_brain)
        EDITH_mouth.runAndWait()
        exit()
    else:
        EDITH_brain = "Sorry, I don't understand what you're saying!"

    print("EDITH: " + EDITH_brain)
    EDITH_mouth.say(EDITH_brain)
    EDITH_mouth.runAndWait()
