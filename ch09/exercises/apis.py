import random
import requests

class Aztro: 
    def __init__(self, sign = 'scorpio', day = 'today'): 
        self.url = f'https://aztro.sameerkumar.website/?sign = {sign} & day = {day}'
    
    def get(self): 
        r = requests.post(self.url)
        response = r.json()
        
        if response.get(): 
            return response.get()
        else:
            return None


x = Aztro(sign = 'scorpio', day = 'today')
print(x.get())

