from ai import AI
from datetime import datetime
from time import sleep as wait
from googlesearch import *
import webbrowser

JARVIS = AI()

class GSP():
    JARVIS.say("Alright Sir")
    wait(1)
    JARVIS.say("What would you like me to search?")
    query = JARVIS.listen()
    print(query)
    chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if query in ["YouTube", "classroom", "tv guide", "TV guide"]:
        JARVIS.say('Okay, opening ' + query)
        wait(1)
        webbrowser.open(query + ".com")
    else:
        JARVIS.say('Okay, opening ' + query)
        wait(1)
        webbrowser.open('google.com/search?q=' + query)