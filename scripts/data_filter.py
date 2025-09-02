from bs4 import BeautifulSoup
import csv 

path = '../data/raw_data/web_data.html'

with open(path, 'r', encoding='utf-8') as f:
    html_f = f.read()

soup = BeautifulSoup(html_f, 'html.parser')
market_banner = soup.find('div', class_='MarketsBanner-marketData')
market_cards = market_banner.find_all('a', class_='MarketCard-container')

cards = []
cards.append(['symbol', 'stock_position', 'change_pct'])

print('Filtering fields from the market banner\n')

for card in market_cards:
    symbol = card.find('span', class_='MarketCard-symbol')
    stock_position = card.find('span', class_='MarketCard-stockPosition')
    change_pct = card.find('span', class_='MarketCard-changesPct')

    symbol = symbol.text.strip()
    stock_position = float(stock_position.text.strip().replace(',', ''))
    change_pct = float(change_pct.text.strip().replace('%', ''))

    cards.append([symbol, stock_position, change_pct])

print('Storing data from the market banner\n')

with open('../data/processed_data/market_data.csv', 'w', encoding='utf-8') as f:
    market_data = csv.writer(f)
    market_data.writerows(cards)

print('Created market_data.csv\n')

latest_news_list = soup.find('ul', class_='LatestNews-list')
latest_news = latest_news_list.find_all('div', class_='LatestNews-container')

news_list = []
news_list.append(['timestamp', 'title', 'link'])

print('Filtering fields from the Latest News section\n')

for news in latest_news:
    timestamp = news.find('time', class_='LatestNews-timestamp').text.strip()
    title = news.find('a', class_='LatestNews-headline').text.strip()
    link = news.find('a', class_='LatestNews-headline')['href']

    news_list.append([timestamp, title, link])

print('Storing data from the Latest News section\n')

with open('../data/processed_data/news_data.csv', 'w', encoding='utf-8') as f:
    news_data = csv.writer(f)
    news_data.writerows(news_list)

print('Created news_data.csv')