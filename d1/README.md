Команды для запуска:

`python code.py alice.txt`

`python code.py siri.txt`

###Отчет
Чтобы научить питон работать с юникодом в windows, пришлось добавить следующие
строки:

```python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
```
Они помогли. Решение было найдено на одном из форумов или на stack overflow.

Сначала нужно импортировать стоп-слова:

```python
from nltk.corpus import stopwords
stopwords = [sw.decode('utf-8') for sw in stopwords.words('russian')]
```

Теперь возьмем все слова, которые встретились в тексте. Это массив `words` из
файла `code.py`, который высылался вместе с домашней работой. Поместим их в
`article_words`, избавившись от всей информации кроме самого слова:

```python
atricle_words = [word[0] for word in words.most_common()]
```

Теперь избавимся от повторений и выведем эту информацию:
```python
atricle_words = Set(atricle_words)
stopwords = Set(stopwords)

print "\nNumber of words without stopwords: ", len(atricle_words - stopwords)
print "Number of lemmas without stopwords: ", len(Set(lemmata) - stopwords)
```

Первая часть домашней работы сделана.

В качестве текста для второй части я выбрал отрывок из книги Питера Уоттса
"Ложная Слепота", он лежит в `siri.txt`. Сири - имя человека, от лица которого в
основном ведется повествование.

Сначала из токенов отбираем те, которые существительные и сохраняем их в массив
`nouns`, приводя перед этим в нормальную форму.

```python
nouns = []
for token in tokens:
	parsed_token = morph.parse(token)[0]
	if 'NOUN' in parsed_token.tag:
		norm = parsed_token.normal_form
		nouns.append(norm)
```

Дальше используем `nltk.FreqDist`, чтобы сосчитать частоты слов. И выводим
информацию в консоль:

```python
nouns = nltk.FreqDist(nouns)
for noun in nouns.most_common()[:10]:
	print(noun[0])
	print(noun[1])
	print(float(noun[1])/len(tokens))
	print('\n')
```

Полностью весь частотный словарь существительных лежит в nouns.
