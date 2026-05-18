import requests
from bs4 import BeautifulSoup

def extract_website_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=15)

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style", "noscript"]):
        script.extract()

    text = soup.get_text(separator=" ")

    cleaned = " ".join(text.split())

    return cleaned[:12000]
