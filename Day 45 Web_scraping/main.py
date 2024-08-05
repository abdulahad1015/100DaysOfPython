from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

titles=[]
links=[]
articles=soup.find_all(name="span",class_="titleline",recursive=True)
for article_tag in articles:
    titles.append(article_tag.getText())
    links.append(article_tag.find(name="a").get("href"))
upvotes =[int(i.getText().split()[0]) for i in soup.find_all(name="span",class_="score")]

# print(titles)
# print(links)
# print(upvotes)

highest=upvotes.index(max(upvotes))

print(titles[highest])
print(links[highest])
print(upvotes[highest])


