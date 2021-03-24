import re 

with open(r"стоп_words.txt", encoding = "utf-8") as date_1:
    text_1 = date_1.read()

text = text_1.split("\n")
stop_words = set(text)

