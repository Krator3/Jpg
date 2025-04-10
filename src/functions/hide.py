import os

def hide_func(jpg_path: str, hide_path: str) -> None:
    # Проверяем существование обоих файлов
    if not os.path.isfile(jpg_path):
        print("JPG файл не существует!")
        return
    if not os.path.isfile(hide_path):
        print("Скрываемый архив не существует!")
        return

    # Читаем и обрабатываем JPG
    try:
        with open(jpg_path, 'rb') as f:
            data = f.read()
            eof_pos = data.index(bytes.fromhex('FFD9')) + 2  # Ищем конец JPEG

        # Удаляем старые скрытые данные, если есть
        if len(data) > eof_pos:
            with open(jpg_path, 'wb') as f_clean:
                f_clean.write(data[:eof_pos])
    except ValueError:
        print("Некорректный JPG файл!")
        return

    # Добавляем данные из архива
    try:
        with open(jpg_path, 'ab') as f, open(hide_path, 'rb') as s:
            f.write(s.read())
    except:
        print("Ошибка при записи данных!")
