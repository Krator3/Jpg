# Код для записи файлов в jpeg/jpg изображение при помощи Python
def hide_func(jpg_path:str, hide_path:str) -> None:
    #print(f"jpg_path: {jpg_path}\nhide_path: {hide_path}")

    # Открываем указанный '.jpg' файл в режиме добавления в бинарном формате (ab)
    with open(jpg_path, 'ab') as f:
        # Открываем файл/архив для скрытия в режиме чтения в бинарном формате (rb)
        with open(hide_path, 'rb') as s:
            # Считываем всё содержимое файла/архива
            data = s.read()
            # Записываем прочитанное содержимое в конец файла '.jpg'
            f.write(data)
