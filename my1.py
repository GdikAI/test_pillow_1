import os
import sys
from PIL import Image, ImageEnhance
import shutil

def process_image(file_path, target_folder):
    """
    Обрабатывает изображение: конвертирует в оттенки серого и увеличивает контраст.
    После обработки сохраняет в целевой папке.
    """
    try:
        # Открытие изображения
        image = Image.open(file_path)
    except IOError:
        print(f"Не удалось открыть изображение {file_path}")
        return

    # Преобразование изображения в оттенки серого
    grayscale = image.convert('L')

    # Увеличение контраста
    enhancer = ImageEnhance.Contrast(grayscale)
    factor = 0.75  # Множитель контраста
    image_output = enhancer.enhance(factor)

    # Получение имени файла и формирование пути для сохранения
    filename = os.path.basename(file_path)
    target_path = os.path.join(target_folder, filename)

    # Сохранение обработанного изображения
    image_output.save(target_path)
    print(f"Изображение {filename} обработано и сохранено в {target_folder}")

def process_images_in_folder(source_folder, target_folder):
    """
    Перебирает все изображения в исходной папке, обрабатывает их и сохраняет в целевой папке.
    """
    # Проверяем, существует ли целевая директория, если нет - создаем её
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Перебираем все файлы в исходной папке
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)

        # Обрабатываем только изображения (можно добавить проверку расширений)

        process_image(source_file_path, target_folder)

# Пример использования
source_directory = r"C:\Users\Владислав\PycharmProjects\test_pillow_1\in"
target_directory = r"C:\Users\Владислав\PycharmProjects\test_pillow_1\out"

process_images_in_folder(source_directory, target_directory)
