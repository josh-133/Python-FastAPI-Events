from typing import Dict
import json as _json

# Grab all events from the events.json file
def get_all_events() -> Dict:
    with open("events.json") as event_file:
        data = _json.load(event_file)
        
    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "This month isn't real"
    
def get_day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "This day isn't real"