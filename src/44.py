import requests
from bs4 import BeautifulSoup
import time

def fetch_and_process():
    # Fetch data from a webpage
    response = requests.get("https://example.com")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for article in soup.find_all("article"):
            title = article.find("h1").text.strip()
            content = article.get_text(strip=True)
            print(f"Title: {title}\nContent:\n{content}\n")

if __name__ == "__main__":
    fetch_and_process()

