import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

titles = []
prices = []
ratings = []

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][1]  # This gives star rating like 'Three'

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

df.to_csv('books_data.csv', index=False)

print("Data scraping complete! Check books_data.csv")
