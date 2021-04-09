#get headers of requested site
import requests
from bs4 import BeautifulSoup

def get_headers(url):   
    response = requests.get(url) 
    print(response.headers)

if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here
    get_headers(url)
