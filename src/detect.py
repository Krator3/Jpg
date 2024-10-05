# Библиотеки
import locale
# Файлы программы
import config

system_language = locale.getlocale()[0]
if config.language != "":
    en_lng = ["en", "en_us", "english", "eng"]
    ru_lng = ["ru", "ru_ru", "russian", "rus"]
    if config.language.lower() in en_lng:
        from lng.English import *
    elif config.language.lower() in ru_lng:
        from lng.Russian import *
elif system_language == "en_US":
    from lng.English import *
elif system_language == "ru_RU":
    from lng.Russian import *
else:
    from lng.English import *
