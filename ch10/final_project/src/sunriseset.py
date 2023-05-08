import requests

class SunRiseSet:
    def __init__(self, lon = None, lat = None):
        '''
        request url with given longitude and latitude to get sunrise/sunset time
        lon: (float) longitude
        lat: (float) latitude
        return None
        '''
        self.url = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&date=today'
    
    def get(self): 
        '''
        get the sunrise and sunset time from the API by making request
        return sunrise, sunset
        '''
        r = requests.get(self.url)
        response = r.json()
        return response['results']['sunrise'], response['results']['sunset']

    def __str__(self):
        '''
        Print out the url source
        '''
        return 'Sunrise/Sunset Generator API url: ' + str(self.url)
    
