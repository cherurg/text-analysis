import urllib.request
from bs4 import BeautifulSoup
import re
import json

games = []
wiki_base = "https://ru.wikipedia.org"


after_link = "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5_%D0%B8%D0%B3%D1%80%D1%8B_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"

for i in range(0, 20):
    page = urllib.request.urlopen(wiki_base + after_link).read()
    soup = BeautifulSoup(page)

    content = soup.find(attrs={'class': "mw-category"})
    for link in content.find_all('a'):
        #games.append("https://ru.wikipedia.org" + link.get('href'))
        games.append(link.get_text())

    after_link = soup(text=re.compile("^следующие 200"))[0].parent.get('href')


with open('article_hrefs.json', 'w', encoding="utf-8") as f:
    data = json.dumps(games, f, ensure_ascii=False)
    f.write(data)

print('saved to article_hrefs.json')
