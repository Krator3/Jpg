# Библиотеки
import locale
# Файлы программы
import config

system_language = locale.getlocale()[0] # Считываем язык системы

# Если в конфиге не установлена переменная языка (по умолчанию пусто)
if config.language != "":
    # Поддерживаемые языки
    en_lng = ["en", "en_us", "english", "eng"] # Возможные обозначения для английского языка
    ru_lng = ["ru", "ru_ru", "russian", "rus"] # Возможные обозначения для русского языка

    # Переводим обозначение в нижний регистр и "подключаем" нужный перевод программы
    if config.language.lower() in en_lng:
        from lng.English import *
    elif config.language.lower() in ru_lng:
        from lng.Russian import *
# Если в конфиге установлена переменная языка
elif system_language == "en_US":
    from lng.English import *
elif system_language == "ru_RU":
    from lng.Russian import *
# Если ничего не подошло, то ставим английский
else:
    from lng.English import *
