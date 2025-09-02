from bs4 import BeautifulSoup
import requests

url = 'https://www.cnbc.com/world/?region=world'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

for link in soup.find_all
