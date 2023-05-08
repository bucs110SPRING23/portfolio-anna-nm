import random
from src import sunriseset
from src import ipaddress


def main():
    random_ip = ""
    for i in range(4): 
        random_ip += str(random.randint(0, 255))
        random_ip += "."
    random_ip = str(random_ip[:-1])
    coor, place = ipaddress.LongLat(random_ip).get()
    sunrise, sunset = sunriseset.SunRiseSet(coor[0], coor[1]).get()
    print('Sunrise today in ' + place[0] + ', ' + place[1] + ' starts at: ' + sunrise)
    print('And sunset is at: '+ sunset)
    
if __name__ == "__main__":
    main()
