from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import time
import random
import os

def human_sleep(min_secs, max_secs):
    time.sleep(random.uniform(min_secs, max_secs))

pwd = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(pwd, "chromedriver")

options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('window-size=1200x600')
options.add_argument('user-agent=Your User Agent Here')
options.add_argument('--no-sandbox')

service = ChromeService(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# insert your URL below
url = 'https://www.zillow.com/poway-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A33.156264987694854%2C%22south%22%3A32.85106756614801%2C%22east%22%3A-116.85498094042971%2C%22west%22%3A-117.21890305957034%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20044%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A275127%2C%22regionType%22%3A8%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3Anull%7D%2C%22beds%22%3A%7B%22min%22%3A3%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'

driver.get(url)
human_sleep(1, 3)
page_soup = BeautifulSoup(driver.page_source, 'html.parser')
human_sleep(2, 4)
driver.quit()

prices = page_soup.find_all('span', {'data-test': 'property-card-price'})
addresses = page_soup.find_all('address', {'data-test': 'property-card-addr'})

for price, address in zip(prices, addresses):
    print(f"Price: {price.text.strip()}, Address: {address.text.strip()}")
