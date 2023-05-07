import random
from src import covid19
from src import ipaddress
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    ip = str(input("Input the IP or type in 0 to generate a random one: "))
    if ip == '0': 
        random_ip = ""
        for i in range(4): 
            random_ip += str(random.randint(0, 255))
            random_ip += "."
        random_ip = str(random_ip[:-1])
        country = ipaddress.IPtoCountry(random_ip).get()
        print(covid19.Covid19(country))
    else: 
        country = ipaddress.IPtoCountry(str(ip)).get()
        print(covid19.Covid19(country))
    
if __name__ == "__main__":
    main()
