# Библиотеки
import os
import sys
import zipfile
import tarfile

# Код для извлечения архива из изображения при помощи Python
def search_func(jpg_path:str) -> None:
    #print(f"jpg_path: {jpg_path}")

    # Открываем указанный '.jpg' файл в режиме чтения бинарных данных
    with open(jpg_path, 'rb') as f:
        path_to_new_archive = "/".join(jpg_path.split("/")[:-1])
        #print(f"path_to_new_archive: {path_to_new_archive}")

        # Считываем всё содержимое файла в переменную content
        content = f.read()

        # Ищем индекс начала последовательности байтов, соответствующих маркеру конца JPEG-файла (FFD9)
        offset = content.index(bytes.fromhex('FFD9'))
        
        # Устанавливаем указатель позиции чтения файла на два байта после найденного маркера FFD9
        f.seek(offset + 2)

        # Открываем новый файл 'newfile.zip' в режиме записи бинарных данных
        with open(f"{path_to_new_archive}/hidden.zip", "wb") as s:
            # Записываем в новый файл все оставшиеся байты после позиции указателя чтения
            s.write(f.read())
        
        # Функция для очистки исходного файла от секрета
        if "-c" in sys.argv or "--clear" in sys.argv:
            with open(jpg_path, 'wb') as o:
                original_file = content[:offset]
                o.write(original_file)
        
        # Проверка на тип спрятанного архива и его исправление
        if zipfile.is_zipfile(f"{path_to_new_archive}/hidden.zip"):
            #print("zip")
            pass
        elif tarfile.is_tarfile(f"{path_to_new_archive}/hidden.zip"):
            #print("tar.gz")
            os.rename(f"{path_to_new_archive}/hidden.zip", f"{path_to_new_archive}/hidden.tar.gz")
        else:
            raise BaseException()

