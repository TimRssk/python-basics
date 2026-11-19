def is_palindrome(s: str) -> bool:
    #Приводим к нижнему регистру и убираем пробелы
    clean_s = s.lower().replace(" ", "")

    #Сравниваем строку с её перевёрнутой версией
    return clean_s == clean_s[::-1]