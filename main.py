import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
page = response.text
soup = BeautifulSoup(page, "html.parser")
articles = soup.find_all(name="h3", class_="title")
print(articles)
titles = []
for article in articles:
    text = article.getText()
    titles.append(text)
result = titles[90:]
print(result)
for item in reversed(result):
    with open("movies.txt", "a") as file:
        file.write(item)
        file.write("\n")


#
# reversed(result) or result[::-1]