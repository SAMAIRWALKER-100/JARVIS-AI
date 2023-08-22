from ai import AI
import jokes
from todo import Todo, Item
from weather import Weather
from calendar_skill import CS
import dateparser
from datetime import datetime
from randfacts import randfacts
from time import sleep as wait
import keyboard

JARVIS = AI()
todo = Todo()
calendar = CS()
calendar.load()

def shapes():
    from shapes import SP

def clock():
    now = datetime.now()
    time = now.hour
    phrase = str("The time is " + time)
    JARVIS.say(phrase)

def googleit():
    from googlepro import GSP

def name():
    JARVIS.say("hi, sm")

def respond():
    JARVIS.say("yes")

def calculator():
    from calculator import CR

def calculators():
    JARVIS.say('Would you like to use addition or subtraction?')
    c = str
    c = JARVIS.listen()
    if c == 'addition':
        def sum(a, b):
            return(a + b)

        JARVIS.say("What is your first number?")
        print("What is your first number?")
        a = int
        a = JARVIS.listen()
        print(a)
        JARVIS.say("What is your second number?")
        print("What is your second number?")
        b = int
        b = JARVIS.listen()
        print(b)

        JARVIS.say(f'Sum of {a} and {b} is {sum(a, b)}')
        print(f'Sum of {a} and {b} is {sum(a, b)}')
    elif c == 'subtraction':
        def diff(a, b):
            return(a - b)

        JARVIS.say('What is your larger number?')
        print('What is your larger number?')
        a = int
        a = JARVIS.listen()
        print(a)
        JARVIS.say('What is your smaller number?')
        print('What is your smaller number?')
        b = int
        b = JARVIS.listen()
        print(b)

        JARVIS.say(f'The difference between {a} and {b} is {diff(a, b)}')
        print(f'The difference between {a} and {b} is {diff(a, b)}')
    elif c == 'neither':
        JARVIS.say("Okay")

def facts():
    fact = randfacts.get_fact()
    print(fact)
    JARVIS.say(fact)

def joke():
    funny = jokes.get_joke()
    print(funny)
    JARVIS.say(funny)

def add_todos()->bool:
    item = Item()
    JARVIS.say("Tell me what to add to the list")
    try:
        item.title = JARVIS.listen()
        todo.new_item(item)
        message = "Added " + item.title
        JARVIS.say(message)
        return True
    except:
        print("oops there was an error")
        return False

def list_todos():
        if len(todo) > 0:
            JARVIS.say("Here are your to do's")
            for item in todo:
                JARVIS.say(item.title)
        else:
            JARVIS.say("The list is empty!")

def weather():
    myweather = Weather()
    forecast = myweather.forecast
    print(forecast)
    JARVIS.say(forecast)

def remove_todos()->bool:
    JARVIS.say("Tell me which item to remove")
    try:
        item_title = JARVIS.listen()
        todo.remove_item(title=item_title)
        message = "Removed " + item_title
        JARVIS.say(message)
        return True
    except:
        print("oops there was an error")
        return False

def rpicam():
    JARVIS.say("activating")
    wait(0.25)
    print("...")
    wait(1.25)
    print("...")
    wait(1)
    print("...")
    wait(0.7)
    from camera import ARPC
    wait(0.5)
    JARVIS.say("Video Saved")

def erpicam():
    JARVIS.say("activating")
    print("...")
    wait(1.25)
    print("...")
    wait(1)
    print("...")
    wait(0.7)
    from cameraeffects import RPC
    wait(0.5)
    JARVIS.say("Video Saved")

def add_event()->bool:
    JARVIS.say("What is the name of the event")
    try:
        event_name = JARVIS.listen()
        JARVIS.say("When is this event?")
        event_begin = JARVIS.listen()
        event_isodate = dateparser.parse(event_begin).strftime("%Y-%m-%d %H: %M: %S")
        JARVIS.say("What is the event description?")
        event_description = JARVIS.listen()
        message = "Ok, adding event " + event_name
        JARVIS.say(message)
        calendar.add_event(begin=event_isodate, name=event_name, describe=event_description)
        calendar.save()
        return True
    except:
        print("oops there was an error")
        return False

def remove_event()->bool:
    JARVIS.say("What is the name of the event you want to remove?")
    try:
        event_name = JARVIS.listen()
        try:
            calendar.remove_event(event_name=event_name)
            JARVIS.say("Event removed successfully")
            calendar.save()
            return True
        except:
            print("Sorry I could not find the event", event_name)
            return False
    except:
        print("oops there was an error")
        return False

def list_events(period):
    this_period = calendar.list_events(period=period)
    if this_period is not None:
        message = "There "
        if len(this_period) > 1:
            message = message + 'are '
        else:
            message = message + ' event'
        message = message + " in the calendar"
        JARVIS.say(message)
        for event in this_period:
            event_date = event.begin.datetime
            weekday = datetime.strftime(event_date, "%A")
            day = str(event.begin.datetime.day)
            month = datetime.strftime(event_date, " %B")
            year = datetime.strftime(event_date, " %Y")
            time = datetime.strftime(event_date, " %I:%M %p")
            name = event.name
            description = event.description
            message = "On " + weekday + " " + day + " of " + month + " " + year + " at " + time
            message = message + ", there is an event called " + name
            message = message + " with an event description of " + description
            JARVIS.say(message)

command = ""
message = now = datetime.now()
hr = now.hour
if hr >= 0 <=12:
    message = "Morning"
if hr >=12 <=17:
    message = "Afternoon"
if hr >=17 <=21:
    message = "Evening"
if hr > 21:
    message = "Night"

message = "Good " + message + " Sir"
JARVIS.say(message)
while True and command != "goodbye":
    try:
        command = JARVIS.listen()
        command = command.lower()
    except:
        print("oops there was an error")
        command = ""
    print("command was:", command)
    
    if command in ["draw me a shape", 'draw a shape', 'draw', 'draw something']:
        shapes()
    if command in ["kill", "abort", "exit", "stop"]:
        quit()
    if command in ["what time is it", "what is the time", "tell me the time", "tell me what the time is", "time", "clock"]:
        clock()
    if command in ["search", "search something", "search something for me", "look something up", "look something up or me", "google something", "google something for me", "look something up for me", "look up something", "look something up", "google", "google this", "open google"]:
        googleit()
    if command in ["sm", "smly", "hi", "hi jarvis"]:
        name()
    if command in ["jarvis", "are you there", "jarvis are you there"]:
        respond()
    if command in ["advanced calculator", "run calculator", "run the advanced calculator"]:
        calculators()
    if command in ["calculator", "pull up calculator", "pull up the calculator"]:
        calculator()
    if command in ["tell me something", "what do you know", "tell me a fact"]:
        facts()
    if command in ["run camera", "camera", "mirror", "run mirror", "turn on the camera", "turn on camera", "run the camera"]:
        rpicam()
    if command in ["run camera with effects", "run camera effects", "camera with effects", "camera effects", "turn on camera with effects", "turn on the camera with effects", "turn on the camera effects", "turn on camera effects"]:
        erpicam()
    if command in ["give me another joke", "say another joke", "tell a another joke", "tell me a another joke", "say something funny", "say a joke", "tell a joke", "tell me something funny", "give me a joke", "tell me a joke"]:
        joke()
    if command in ["what is the weather", "what's the weather", "whats the weather", "give me the weather", "tell me the weather", "what's the weather like", "whats the weather like", "tell me what the weathers like", "tell me what the weather's like", "tell me what the weather is like", "what is the weather like"]:
        weather()
    if command in ["add to-do", "add to do", "add item"]:
        add_todos()
    if command in ["list todos", "list todo", "list to do", "list to-do", "list to do's" "list todo's", "list to dos", "list to-dos", "list to-do's", "list items", "list item's", "list item", "list two dues", "list two due", "list two due's", "list two-due", "list two-dues", "list two-due's", "list twodue", "list twodues", "list twodue's", "list twodos", "list twodo", "list twodo's", "list two do", "lit two dos", "list two do's", "list two-do", "list two-dos", "list two-do's", "list todue", "list todues", "list todue's", "list to due", "list to dues", "list to due's"]:
        list_todos()
    if command in ["remove todo", "remove item", "mark done", "remove to-do", "remove items", "remove todos", "remove todo's", "remove item's", "remove to-dos", "remove to-do's", "delete items", "delete item", "delete item's", "delete todos", "delete todo", "delete todos", "delete to dos", "delete to do's", "delete to do"]:
        remove_todos()
    if command in ['good morning', "good afternoon", "good evening", "good night", "hello", "hello jarvis"]:
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <=12:
            message = "Morning"
        if hr >=12 <=17:
            message= "Afternoon"
        if hr >=17 <=21:
            message = "Evening"
        if hr > 21: message = "Night"

        message = "Good " + message + " Sir"
        JARVIS.say(message)

    if command in ["add event", "add events", "add event's", "add to calendar", "add to the calendar", "add new event", "add new events", "add new event's", "new event", "new events", "new event's"]:
        add_event()
    if command in ["delete event", "remove event", "cancel event", "delete events", "remove events", "cancel events", "delete event's", "remove event's", "cancel event's"]:
        remove_event()
    if command in ["list events for the month", "list event for the month", "list event's for the month", "what's on this month", "whats on this month", "what's coming up this month"]:
        list_events(period='this month')
    if command in ["list events for the week", "list event for the week", "list event's for the week", "what's on this week", "whats on this week", "what's coming up this week"]:
        list_events(period='this week')
    if command in ["list all events"]:
        list_events(period='all')
    if command in ["goodbye", "bye", "see you later", "later", "goodnight", "night"]:
        now = datetime.now()
        hr = now.hour
        if hr > 18: 
            message = "night"
            phrase = "Good" + message + " Sir"
            JARVIS.say(phrase)
        else:
            JARVIS.say("Goodbye Sir")