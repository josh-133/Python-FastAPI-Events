import requests as _requests
import bs4 as _bs4

def _generate_month_url(month: str, day: int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url
