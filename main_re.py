"""
1 - открыть файл т тзвечь обертку
2 - прочитать обертку и сохранить  в переменную
3 - убрать из текста не буквы
"""

import re 
from collections import Counter

with open(r"WWW.txt", encoding = "utf-8") as date:
    text = date.read()

text = text.lower()
edited_text = re.findall(r"[а-я]+", text)
text = re.sub("ё", "е", text)
resualt = dict(Counter(edited_text).most_common(20))

print(resualt)

