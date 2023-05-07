import random 
import requests

class IPaddress: 
    def __init__(self, ip) -> None:
        self.api_url = f"https://ipvigilante.com/json/{ip}"

    def get(self): 
        r = requests.get(self.api_url)
        response = r.json()
        