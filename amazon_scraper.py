import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")

titles = []

for book in books:
    titles.append(book.text)

df = pd.DataFrame(titles, columns=["Book Title"])

df.to_csv("books.csv", index=False)

print("Saved to books.csv")