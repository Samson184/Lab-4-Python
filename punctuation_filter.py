#  Учасник 3: Модуль очищення від розділових знаків

import string


def clean_words(raw_words: list[str]) -> list[str]:

    # Приймає список слів/фрагментів тексту, видаляє знаки пунктуації
    # згідно з умовою (розділові знаки опускаються) та повертає список чистих слів.

    cleaned_words = []
    
    # Стандартний набір розділових знаків ASCII + специфічні символи (тире, лапки тощо)
    punctuation_symbols = string.punctuation + "—«»„“”…"
    
    # Таблиця для швидкого видалення знаків через translate
    translator = str.maketrans("", "", punctuation_symbols)
    
    for token in raw_words:
        # Видаляємо всі розділові знаки зі слова
        word = token.translate(translator).strip()
        
        # Залишаємо тільки непорожні слова (якщо токен складався лише з розділових знаків, він відсіється)
        if word:
            cleaned_words.append(word)
            
    return cleaned_words


# Автономний тест модуля (для перевірки та скріншота у звіт)
if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТУВАННЯ МОДУЛЯ ОЧИЩЕННЯ ТЕКСТУ (УЧАСНИК 3)")
    print("=" * 60)
    
    # Тестовий набір даних, що імітує результат zчитування з файлу TF1_1
    sample_raw_tokens = [
        "Лабораторна,", "робота", "№4:", "обробка", "текстових", "файлів!",
        "—", "мова", "програмування", "Python...", "(версія", "3.x);", 
        "«текст»", "і", "розділові", "знаки."
    ]
    
    print("\n[Вхідні фрагменти з файлу]:")
    print(sample_raw_tokens)
    
    cleaned_result = clean_words(sample_raw_tokens)
    
    print("\n[Результат після очищення (розділові знаки видалено)]:")
    print(cleaned_result)
    
    print(f"\nКількість вхідних елементів: {len(sample_raw_tokens)}")
    print(f"Кількість слів після очищення: {len(cleaned_result)}")
    print("=" * 60)