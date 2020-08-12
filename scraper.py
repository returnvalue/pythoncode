# Building The Scraping Script
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)

# Parsing Html Markup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

print(quotes)

# Beautiful Soup text property
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)

# More Granular
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)

# Using an inner loop
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')

# Web Scraping More Than One Page
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{count}:  {itemPrice} for the {itemName}')
    count += 1
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{count}:  {itemPrice} for the {itemName}')
        count += 1
