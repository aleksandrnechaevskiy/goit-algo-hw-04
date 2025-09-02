import os
import shutil

def recursive_file_copy(source_path, destination_path):
    """
    Рекурсивно копіює файли з вихідної директорії в директорію призначення,
    сортуючи їх по піддиректоріях, названих за розширенням файлу.

    :param source_path: Шлях до вихідної директорії.
    :param destination_path: Шлях до директорії призначення.
    """
    try:
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)

            if os.path.isdir(item_path):
                # Рекурсивний виклик для піддиректорій
                recursive_file_copy(item_path, destination_path)
            elif os.path.isfile(item_path):
                # Обробка файлів
                _, extension = os.path.splitext(item)
                extension = extension.lstrip('.')  # Видаляємо крапку
                if not extension:
                    extension = 'no_extension'  # Для файлів без розширення

                # Створення піддиректорії для розширення
                target_dir = os.path.join(destination_path, extension)
                os.makedirs(target_dir, exist_ok=True)

                # Копіювання файлу
                shutil.copy2(item_path, target_dir)
                print(f'Файл {item_path} скопійовано до {target_dir}')

    except FileNotFoundError:
        print(f"Помилка: Вихідна директорія '{source_path}' не знайдена.")
    except PermissionError:
        print(f"Помилка: Немає дозволу на доступ до '{source_path}'.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def main():
    """
    Головна функція для запиту шляхів у користувача та запуску програми.
    """
    # Запит шляху до вихідної директорії
    source_path = input("Скопіюйте і вставте сюди шлях до директорії джерела: ").strip()

    # Запит шляху до директорії призначення
    destination_path = input("Скопіюйте і вставте сюди шлях до директорії призначення (залишіть порожнім для 'dist'): ").strip()

    # Використання шляху за замовчуванням, якщо користувач нічого не ввів
    if not destination_path:
        destination_path = 'dist'

    # Перевірка існування вихідної директорії
    if not os.path.isdir(source_path):
        print(f"Помилка: Вихідна директорія '{source_path}' не існує.")
        return

    # Виклик рекурсивної функції
    recursive_file_copy(source_path, destination_path)

if __name__ == "__main__":
    main()