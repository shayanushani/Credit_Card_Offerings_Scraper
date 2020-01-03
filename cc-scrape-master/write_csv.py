import csv
import os
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper import Scraper
from sheets import write_to_google_sheet

def get_driver():
    options = Options()
    if platform == 'darwin':
        driver_path = 'chromedriver'

    elif platform == 'linux':
        driver_path = './bin/chromedriver-linux'
        options.binary_location = './bin/headless-chromium-linux'
        options.add_argument('--disable-dev-shm-usage')

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    return webdriver.Chrome(driver_path, chrome_options=options)


def write_output(data):
    with open('data.csv', mode='w') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Header
        writer.writerow(['Credit Card Bank Name', 'Credit Card Name', 'Credit Card Image Link', 'Credit Card Details - Body Information', 'Credit Card APY', 'Credit Card Fee', 'Credit Card Apply Link'])
        # Body
        for row in data:
            writer.writerow(row)

def fetch_data():
    driver = get_driver()
    # Begin scraper
    scraper = Scraper(driver)

    scraper.get_citi_offers()
    print('done scraping citi')
    scraper.get_discover_offers()
    print('done scraping discover')
    scraper.get_capital_one_offers()
    print('done scraping capital one')
    scraper.get_chase_offers()
    print('done scraping chase')
    scraper.get_us_bank_offers()
    print('done scraping us bank')
    scraper.get_wells_fargo_offers()
    print('done scraping wells fargo')
    scraper.get_barclays_offers()
    print('done scraping barclays')
    scraper.get_american_express_offers()
    print('done scraping am ex')
    scraper.get_bank_of_america_offers()
    print('done scraping bank of america')
    
    # End scraper

    driver.quit()
    return scraper.all_card_offers

def scrape():
    data = fetch_data()
    write_to_google_sheet(data)
    


