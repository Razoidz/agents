from re import findall
from urllib import response

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ilorin.info/fullnews.php?id=39283")
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html,"html.parser")
headlines = soup.find_all("h2")
for headline in headlines:
    if headline.find('a') is None:
        print(headline.text.strip())