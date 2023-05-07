import requests
import ipaddress
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Covid19: 
    def __init__(self, country = None): 
        self.api_url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
    
    def get(self): 
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        r = requests.get(self.api_url, headers=headers)
        response = r.json()['All']
        confirmed = "Confirmed: " + str(response['confirmed'])
        return confirmed