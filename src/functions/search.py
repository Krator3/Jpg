import os
import sys

def search_func(jpg_path: str) -> None:
    if not os.path.isfile(jpg_path):
        print("JPG файл не существует!")
        return

    with open(jpg_path, 'rb') as f:
        path_to_new_archive = "/".join(jpg_path.split("/")[:-1])
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9')) # Ищем конец JPG файла
        f.seek(offset + 2)

        # Ищем скрытые данные
        hidden_data = f.read()
        if not hidden_data:
            print("Нет скрытых данных")
            return

        # Извлекаем скрытый архив, если он есть
        hidden_path = f"{path_to_new_archive}/hidden.zip"
        with open(hidden_path, "wb") as s:
            s.write(hidden_data)

        # Очистка, если указан специальный флаг
        if "-c" in sys.argv or "--clear" in sys.argv:
            with open(jpg_path, 'wb') as o:
                original_file = content[:offset + 2]
                o.write(original_file)
