from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from bs4 import BeautifulSoup
import time
import random

def human_sleep(min_secs, max_secs):
    time.sleep(random.uniform(min_secs, max_secs))

# Path to your EdgeDriver
driver_path = r'C:\Users\nayan\Downloads\edgedriver_win64\msedgedriver.exe'

# Set up Selenium and browser options
options = EdgeOptions()
options.add_argument('--headless')  # Run in headless mode (no browser UI)
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('window-size=1200x600')
options.add_argument('user-agent=Your User Agent Here')
options.add_argument('--no-sandbox')

# Create the driver
service = EdgeService(driver_path)
driver = webdriver.Edge(service=service, options=options)

# Zillow URL
url = 'https://www.zillow.com/poway-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A33.156264987694854%2C%22south%22%3A32.85106756614801%2C%22east%22%3A-116.85498094042971%2C%22west%22%3A-117.21890305957034%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20044%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A275127%2C%22regionType%22%3A8%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3Anull%7D%2C%22beds%22%3A%7B%22min%22%3A3%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'

# Open the page
driver.get(url)

human_sleep(1, 3)

# Get the page source and parse with BeautifulSoup
html = driver.page_source
page_soup = BeautifulSoup(html, 'html.parser')

human_sleep(2, 4) 

# Close the driver
driver.quit()

# Example of extracting data: Prices, Addresses
prices = page_soup.find_all('span', {'data-test': 'property-card-price'})
addresses = page_soup.find_all('address', {'data-test': 'property-card-addr'})

# Print the prices and addresses
for price, address in zip(prices, addresses):
    print(f"Price: {price.text.strip()}, Address: {address.text.strip()}")

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# import random

# def human_sleep(min_secs, max_secs):
#     time.sleep(random.uniform(min_secs, max_secs))

# # Path to your EdgeDriver
# driver_path = r'C:\Users\nayan\Downloads\edgedriver_win64\msedgedriver.exe'

# # Set up Selenium and browser options
# options = EdgeOptions()
# options.add_argument('--headless')  # Run in headless mode (no browser UI)
# options.add_argument('--disable-gpu')  # Disable GPU acceleration
# options.add_argument('window-size=1200x600')
# options.add_argument('user-agent=Your User Agent Here')
# options.add_argument('--no-sandbox')

# # Create the driver
# service = EdgeService(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# # Zillow URL
# url = 'https://www.zillow.com/poway-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A33.156264987694854%2C%22south%22%3A32.85106756614801%2C%22east%22%3A-116.85498094042971%2C%22west%22%3A-117.21890305957034%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20044%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A275127%2C%22regionType%22%3A8%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3Anull%7D%2C%22beds%22%3A%7B%22min%22%3A3%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'

# # Function to scroll and extract listings
# def scroll_and_extract(url):
#     driver.get(url)
#     human_sleep(5, 10)
    
#     all_listings = []
    
#     while True:
#         # Get the page source and parse with BeautifulSoup
#         html = driver.page_source
#         page_soup = BeautifulSoup(html, 'html.parser')
        
#         # Extract data: Prices, Addresses
#         prices = page_soup.find_all('span', {'data-test': 'property-card-price'})
#         addresses = page_soup.find_all('address', {'data-test': 'property-card-addr'})
        
#         for price, address in zip(prices, addresses):
#             all_listings.append((price.text.strip(), address.text.strip()))
        
#         # Scroll down to load more listings
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         human_sleep(2, 4)  # Wait for new elements to load

#         # Use WebDriverWait for the "Next" button
#         try:
#             next_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Next page"]'))
#             )
#             next_button.click()
#             human_sleep(2, 4)  # Wait for the next page to load
#         except Exception as e:
#             print(f"No more pages or error: {e}")
#             break
    
#     return all_listings

# # Call the function to extract listings
# listings = scroll_and_extract(url)

# # Close the driver
# driver.quit()

# # Print the extracted listings
# for price, address in listings:
#     print(f"Price: {price}, Address: {address}")