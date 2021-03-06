def is_valid_ip(given_str: str) -> bool:
    if not given_str:
        return False

    # ровно 3 точки
    if given_str.count(".") != 3:
        return False
    
    # 255.255.255.255
    if len(given_str) > 15:
        return False

    # нет пробелов
    if given_str.count(" ") > 0:
        return False

    # нет букв
    for i in given_str:
        if i.isalpha():
            return False

    # не меньше нуля и не больше 255
    given_str_list = given_str.split(".")
    for i in given_str_list:
        if int(i) > 255 or int(i) < 0:
            return False

assert is_valid_ip("") == False, "Пустая строка не IP"
assert is_valid_ip("a") == False, "IP не содержит букв"
assert is_valid_ip("192.45.65.-1") == False, "IP не болше 255"
assert is_valid_ip("125.51.54.8.23") == False, "IP больше 4"
assert is_valid_ip(" 45.123.235.42") == False, "IP не содержит пробелов"
assert is_valid_ip("192.45.65.256") == False, "IP не болше 255"