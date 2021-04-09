#get headers of requested site
import requests
from bs4 import BeautifulSoup
import sys

def get_headers(url):   
    response = requests.get(url)

    print(response.headers)

#def save_data(url,path):
    #print("headers are getting saved in ", path)
    #response = requests.get(url)
    #sys.stdout = open(path, "w")
    #print(response.headers) 
    #sys.stdout.close()

  
if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here
    get_headers(url)
