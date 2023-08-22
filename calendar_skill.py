from ics import Calendar, Event
from pathlib import Path
import os
import yaml
from datetime import datetime
from dateutil.relativedelta import *
import pytz

calendar_filename = 'docs/myfile.ics'
calendar_datafile = 'myfile.yml'

class CS():
    c = Calendar()

    def __init__(self):
        ''' Print a nice banner '''
        print("")
        print("*"*50)
        print("Calendar Skill Loaded")
        print("*"*50)

    def add_event(self, begin:str, name:str, description:str=None)->bool:
        ''' adds and event to the calendar '''
        e = Event()
        e.name = name
        e.begin = begin
        e.description = description
        try:
            self.c.events.add(e)
            return True
        except:
            print("there was a problem adding the event, sorry.")
            return False

    def remove_event(self, event_name:str):
        ''' Removes the event from the calendar '''

        for event in self.c.events:
            if event.name == event_name:
                self.c.events.remove(event)
                print("removing event:", event_name)
                return True

        print("Sorry could not find that event:", event_name)
        return False
    
    def parse_to_dict(self):
        dict = []
        for event in self.c.events:
            my_event = {}
            my_event['begin'] = event.begin.datetime
            my_event['name'] = event.name
            my_event['description'] = event.description
            dict.append(my_event)
        return dict

    def save(self):
        with open(calendar_filename, 'w') as my_file:
            my_file.writelines(self.c)

        if self.c.events == set():
            print ("No Events - Removing YAML file")
            try:
                os.remove(calendar_datafile)
            except:
                print("oops couldn't delete the YAML file")
        else:
            with open(calendar_datafile, 'w') as outfile:

                yaml.dump(self.parse_to_dict(), outfile, default_flow_style=False)

    def load(self):
        ''' load the Calendar data from the YAML file '''
        filename = calendar_datafile
        my_file = Path(filename)
        if my_file.is_file():
            stream = open(filename, 'r')
            events_list = yaml.load(stream)
            for item in events_list:
                e = Event()
                e.begin = item['begin']
                e.description = item['description']
                e.name = item['name']
                self.c.events.add(e)
        else:
                print("file does not exist")

    def list_events(self, period:str=None)->bool:
        ''' Lists the upcoming events
            if `period` is left empty it will default to today
            other options are:
            `all` - lists all events in the calendar
            `this week` - lists all the events this week
            `this month` - lists all the events this month
        '''

        if period == None:
            period = "this week"

        if self.c.events == set():
            print("No Events In Calendar")
            return False
        else:
            event_list = []
            now = pytz.utc.localize(datetime.now())
            if period == "this week":
                nextperiod = now+relativedelta(week=+1)
            if period == "this month":
                nextperiod = now+relativedelta(months=+1)
            if period == "all":
                nextperiod = now+relativedelta(years=+100)
            for event in self.c.events:
                event_date = event.begin.datetime
                if (event_date >= now) and (event_date <= nextperiod):
                    event_list.append(event)
            return event_list