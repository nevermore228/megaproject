from bs4 import BeautifulSoup
import requests
import re

url = 'https://volga.news/'
page = requests.get(url)
#print(page.status_code)

filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
allNews = soup.findAll('li', class_="b-news-item")
#print(allNews)

for data in allNews:
    if data.find('div', class_='b-news-item__title g-bold') is not None:
        filteredNews.append(data.text)
#print(filteredNews)
for data in filteredNews:
    re.sub("^\s+|\n|\r|\s+$", '', data)
    print(data)