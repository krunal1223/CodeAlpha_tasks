# Step 1: Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 2: Define URL and get page content
url = 'http://books.toscrape.com/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Create empty lists to hold data
titles = []
prices = []
ratings = []

# Step 4: Find all book containers
books = soup.find_all('article', class_='product_pod')

# Step 5: Extract info from each book
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][1]  # This gives star rating like 'Three'

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

# Step 6: Store data in a table using pandas
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

# Step 7: Save data to a CSV file
df.to_csv('books_data.csv', index=False)

print("✅ Data scraping complete! Check books_data.csv")
