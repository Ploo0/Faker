import os
import random
from faker import Faker

# Путь к папке с шаблонами текста и папке для сохранения сгенерированных текстов
templates_folder = 'templates'
output_folder = 'generated_texts'

# Создаем папку для сохранения сгенерированных текстов, если её нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Инициализация объекта Faker
faker = Faker('ru_RU')

# Функция для чтения шаблонов из текстовых файлов
def load_templates(folder):
    templates = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()
                sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
                templates.extend(sentences)
    return templates

# Функция для создания случайного текста
def generate_text(templates, num_words):
    generated_text = ""
    while len(generated_text.split()) < num_words:
        sentence = random.choice(templates)
        generated_text += " " + sentence
    # Удаляем лишние слова в конце, чтобы текст был не длиннее указанного количества слов
    words = generated_text.split()
    generated_text = " ".join(words[:num_words])
    # Заменяем любой знак в конце предложения на точку
    generated_text = generated_text.rstrip(".,?!") + "."
    return generated_text

while True:
    num_words_input = input("Введите количество слов в сгенерированном тексте (или 'exit' для выхода): ")
    if num_words_input.lower() == 'exit':
        print("Выход из программы.")
        break
    try:
        num_words = int(num_words_input)
        if num_words > 0:
            generated_text = generate_text(load_templates(templates_folder), num_words)
            print("Сгенерированный текст:")
            print(generated_text)

            # Сохраняем сгенерированный текст в файл
            output_filename = os.path.join(output_folder, 'generated_text.txt')
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(generated_text)
            
            print(f"Сгенерированный текст сохранен в файл: {output_filename}")
        else:
            print("Ошибка: Количество слов должно быть больше нуля.")
    except ValueError:
        print("Ошибка: Введите целое положительное число или 'exit' для выхода.")
