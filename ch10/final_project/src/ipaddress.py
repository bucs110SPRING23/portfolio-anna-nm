import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class IPtoCountry: 
    def __init__(self, ip):
        self.api_url = f"https://ipvigilante.com/json/{ip}"

    def get(self): 
        r = requests.get(self.api_url, verify=False)
        if r.status_code == 200:
            response = r.json()
            country = str(response['data']['country_name'])
            print(country)
            return country
        else:
            print("Error from server: " + str(r.content))
        #response = r.json()
        