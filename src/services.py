from typing import Dict
import json as _json

def get_all_events() -> Dict:
    with open("events.json") as event_file:
        data = _json.load(event_file)
        
    return data