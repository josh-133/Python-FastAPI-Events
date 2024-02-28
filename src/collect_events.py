from typing import Iterator, Dict
import datetime as _dt
import json as _json

import scraper as _scraper

# Get the date range for create_events_dict function
def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]: 
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n) # yield here returns a generator object to the one who calls the function which contains yield (create_events_dict function in this case)

# This function goes through a date range and returns all events that occurred in that time frame
def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020,1,1)
    end_date = _dt.date(2020,8,1)
    
    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()
            
        events[month][date.day] = _scraper.events_of_the_day(month,date.day)
        
    return events

# This runs the create_events_dict() function and dumps all the event data into the
# events_file json file.
if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", mode="w") as events_file:
        _json.dump(events, events_file, ensure_ascii=False)