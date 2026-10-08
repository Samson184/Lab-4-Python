def count_words_in_file(path="TF1_2.txt"):
    """Рахує слова (непорожні рядки) і порожні рядки у файлі."""
    words = 0
    empty = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    words += 1
                else:
                    empty += 1
    except FileNotFoundError:
        print(f"Помилка: файл {path} не знайдено")
        return None
    return {"words": words, "empty_lines": empty}


def print_analytics(path="TF1_2.txt"):
    result = count_words_in_file(path)
    if result is None:
        return
    print(f"Всього записано слів: {result['words']}")
    if result["empty_lines"]:
        print(f"Увага: знайдено порожніх рядків: {result['empty_lines']}")
    else:
        print("Порожніх рядків немає")


if __name__ == "__main__":
    print_analytics()