import wikipedia
import json

wikipedia.set_lang("ru")

file = open("article_hrefs.json")
titles = json.load(file)
file.close()

counter = 0
for title in titles:
    try:
        page = wikipedia.page(title)
        f = open('content/' + title, 'w', encoding='utf-8')
        f.write(page.content)
        f.close()
        counter += 1
        print(counter)
    except:
        None
