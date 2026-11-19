from collections import Counter

def word_count(text: str) -> dict[str, int]:
    # Приводим к нижнему регистру и разбиваем на слова по пробелам
    words = text.lower().split()

    # Counter автоматически считает частоту элементов
    counts = Counter(words)

    return dict(counts)