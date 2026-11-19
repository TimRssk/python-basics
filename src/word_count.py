def word_count(text: str) -> dict[str, int]:
    # Приводим к нижнему регистру и разбиваем на слова по пробелам
    words = text.lower().split()

    counts = {}
    for word in words:
        # Если слова нет в словаре, get вернёт 0. Прибавляем 1.
        counts[word] = counts.get(word, 0) + 1

    return counts