from main import Open

def save_and_display_words():
    file2_name = "TF1_2.txt"
    
    # Список очищених слів (у повному проєкті вони передаються з модуля фільтрації)
    cleaned_words = [
        "Hello", "world", "This", "is", "a", "test", "string",
        "designed", "for", "practical", "work", "number",
        "4", "Lets", "check", "how", "it", "works", "student"
    ]
    
    # 1. Відкриття файлу TF1_2.txt у режимі запису ("w")
    file_2_w = Open(file2_name, "w")
    
    if file_2_w is not None:
        for word in cleaned_words:
            # Записуємо кожне слово на окремому рядку
            if word.strip():  # Захист від запису порожніх рядків для тестів
                file_2_w.write(word + "\n")
                
        print("Information was successfully added to TF1_2.txt!")
        file_2_w.close()
        print("File TF1_2.txt was closed!")

    print("-" * 30)

    # 2. Відкриття файлу TF1_2.txt у режимі читання ("r") та друк у консоль
    file_3_r = Open(file2_name, "r")
    
    if file_3_r is not None:
        print("New sequence (content of TF1_2.txt by lines):")
        for line in file_3_r:
            print(line.strip())  # strip() прибирає зайві переноси рядків при друці
            
        file_3_r.close()
        print("File TF1_2.txt was closed!")

if __name__ == "__main__":
    save_and_display_words()
