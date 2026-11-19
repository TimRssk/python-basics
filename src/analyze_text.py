import sys
from is_palindrome import is_palindrome
from word_count import word_count

def main():
    # Проверяем, передал ли пользователь путь к файлу
    if len(sys.argv) < 2:
        print("Ошибка: Укажите путь к файлу. Пример: python src/analyze_text.py data/sample.txt")
        return

    filepath = sys.argv[1]

    try:
        # Открываем и читаем файл
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
        return

    # 1. Считаем строки, слова и символы
    lines_count = len(text.splitlines())
    words = text.split()
    words_count = len(words)
    chars_count = len(text)

    print(f"--- Статистика файла: {filepath} ---")
    print(f"Строк: {lines_count}")
    print(f"Слов: {words_count}")
    print(f"Символов: {chars_count}")

    # 2. Топ-5 слов
    counts = word_count(text)
    # Сортируем словарь по значениям (частоте) по убыванию и берём первые 5
    top_5 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]

    print("\nТоп-5 самых частых слов:")
    for word, count in top_5:
        print(f"  {word}: {count}")

    # 3. Проверка на палиндром (проверяем весь текст)
    # (Для длинного текста это почти всегда False, но для проверки кода сойдёт)
    print(f"\nЯвляется ли текст палиндромом: {is_palindrome(text)}")

if __name__ == "__main__":
    main()