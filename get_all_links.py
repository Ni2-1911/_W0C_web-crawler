#GET ALL ANCHOR TAGS
import requests
from bs4 import BeautifulSoup



def get_links(u):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", "Upgrade-Insecure-Requests": "1"}  
        
                
        response = requests.get(u , headers = header)
        soup = BeautifulSoup(response.text,'html.parser')

        for link in soup.find_all('a'):
                print(link.get('href'))


if __name__ == "__main__":
        url = input('ENTER YOUR TARGET URL HERE')
        get_links(url)
