import requests

class LongLat: 
    def __init__(self, ip):
        '''
        request url with given IP address
        ip: (str) given IP address
        return None
        '''
        self.api_url = f"https://geolocation-db.com/json/{ip}"

    def get(self): 
        '''
        get the longitude, latitude, and place from the ip given 
        return coordinates and place if found, 
            or Place not found if not exist
        '''
        r = requests.get(self.api_url)
        if r.status_code == 200:
            response = r.json()
            longitude = response['longitude']
            latitude = response['latitude']
            city = response['city']
            country = response['country_name']
            if city == None: 
                city = ''
            if country == None: 
                country = ''
            place = [city, country]
            if longitude != "Not found" or latitude != "Not found":
                longitude, latitude = float(longitude), float(latitude)
                coor = [longitude, latitude]
                return coor, place
            else:
                return "Place not found!"
        else:
            print("Error from server: " + str(r.content))
            return 0,0
        
    def __str__(self):
        '''
        Print out the url source
        '''
        return 'Sunrise/Sunset Generator API url: ' + str(self.url)