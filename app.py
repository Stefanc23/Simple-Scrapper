import requests
from bs4 import BeautifulSoup

query = input("Query: ")

URL = "https://www.tokopedia.com/search?q=" + query + "&source=universe&st=product&navsource=home"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

titles = soup.findAll(attrs={"class": "css-18c4yhp"})
prices = soup.findAll(attrs={"class": "css-rhd610"})

for i in range(len(titles)):
  titles[i] = titles[i].get_text().strip()
  prices[i] = prices[i].get_text().strip()

for i in range(len(titles)):
  print('\n' + titles[i] + '\n' + prices[i] + '\n')