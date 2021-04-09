#here code for get html in preetified form
import requests
from bs4 import BeautifulSoup
import re

def get_source_code(url):
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    a = soup.prettify
    lst = re.findall('\S+@\S+', str(a))     
    print(lst)

if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here
    get_source_code(url)


