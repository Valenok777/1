"""
1 - открыть файл и извечь обертку
2 - прочитать обертку и сохранить  в переменную
3 - все буквы заменить строчными
4 - заменить ё на е
5 - убрать из текста не буквы 
6 - все предлоги сохрарить в переменную
7 - убрать предлоги
"""

import re 
from collections import Counter
import stop_words_1 as sw
import time

time_start = time.time()

with open(r"Мастер и Маргарита.txt", encoding = "utf-8") as date:
    text = date.read()

text = text.lower()
text = re.sub("ё", "е", text)
#список
edited_text = re.findall(r"[а-я]+", text)

for i in edited_text:
	if i in sw.stop_words:
		edited_text.remove(i)


resualt = dict(Counter(edited_text).most_common(20))

time_stop = time.time()

print(round(time_stop - time_start))
print(resualt)