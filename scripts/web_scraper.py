from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

url = 'https://www.cnbc.com/world/?region=world'
driver = webdriver.Chrome()
driver.get(url)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, 'MarketCard-row')))

soup = BeautifulSoup(driver.page_source, 'html.parser')
market_banner = soup.find('div', class_='MarketsBanner-marketData').prettify()
latest_news = soup.find('ul', class_='LatestNews-list').prettify()

with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as f:
    f.write(str(market_banner))
    f.write(str(latest_news))