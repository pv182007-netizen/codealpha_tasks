import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://books.toscrape.com/"

response = requests.get(URL, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a.get("title", "").strip()
    price = book.select_one(".price_color").get_text(strip=True)
    availability = book.select_one(".availability").get_text(" ", strip=True)
    rating = book.select_one("p.star-rating").get("class", ["", ""])[1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)

print("Web scraping completed successfully!")
print(f"Books collected: {len(df)}")
print("CSV file saved as: books_data.csv")
print(df.head())
