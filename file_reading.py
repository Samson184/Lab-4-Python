from main import Open


def read_words(file_name="TF1_1.txt"):
    """Частина б), етап 1: читає файл і розбиває вміст на слова."""
    file = Open(file_name, "r")
    if file is None:
        return []

    text = file.read()
    file.close()
    return text.split()


if __name__ == "__main__":
    words = read_words()
    print("Прочитано слів:", len(words))
    print(words)

    print("--- Перевірка помилки ---")
    read_words("no_such_file.txt")