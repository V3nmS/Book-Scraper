import requests
from bs4 import BeautifulSoup

resp = requests.get("https://quotes.toscrape.com/", timeout=10)
resp.raise_for_status
soup = BeautifulSoup(resp.text, "html.parser")

for q in soup.select("div.quote"):
    text = q.select_one("span.text").get_text(strip=True)
    author = q.select_one("small.author").get_text(strip=True)
    print(f"{author}: {text}")

next_link = soup.select_one("li.next a")
print("next:", next_link["href"] if next_link else None)
