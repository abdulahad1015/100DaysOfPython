import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(URL)
yc_web_page=response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
titles=[i.getText() for i in soup.findAll(name="h3")]
titles = titles[::-1]

with open("Movies.txt",mode="w",encoding="utf-8") as file:
    for i in titles:
        file.write(f"{i}\n")
# print(soup.prettify())

