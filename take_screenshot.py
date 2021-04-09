from selenium import webdriver

def take_screenshot(url):
    driver = webdriver.Chrome(executable_path='/Users/nitukumari/Desktop/web-crawler/chromedriver')

    driver.get(url)

    driver.get_screenshot_as_file( 'main_page.png')
    driver.close()

if __name__ == "__main__":
    url = input('ENTER YOYR TARGET URL HERE: ')
    take_screenshot(url)
