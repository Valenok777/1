import my_test
def is_palindrom(text: str) -> bool:
    upper_text = text.upper()
    letters_upper_text = upper_text.replace(',', '')
    letters_upper_text = letters_upper_text.replace('!', '')
    letters_upper_text = letters_upper_text.replace('.', '')
    letters_upper_text = letters_upper_text.replace('-', '')
    letters_upper_text = letters_upper_text.replace(' ', '')
    return letters_upper_text == letters_upper_text[::-1]

is_palindrom("О, лета тело!")

assert is_palindrom("О, лета тело!") == True, "eeee"