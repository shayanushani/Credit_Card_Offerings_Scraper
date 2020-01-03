from sys import platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def handler(event, context):
    
    print('sdfs')
    print('_________________________________________')

    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://api.ipify.org?format=json')
    print(driver.page_source)


if __name__ == '__main__':
    handler(None, None)