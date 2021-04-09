#here code for get html in preetified form
import requests
from bs4 import BeautifulSoup


def get_source_code(url):
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    print(soup.prettify)

def get_page_text(url):
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    page_text = soup.get_text()
    print(page_text)

if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here
    get_page_text(url)


