import re
import time
max_buffer_len = 1000  # максимальный размер рабочего буфера
try:
    filePath = input('Введите путь к файлу: ')  # Получаем путь к файлу.
    with open(filePath, "r", encoding="utf-8") as f:  # открываем файл
        buffer = f.read(max_buffer_len)  # читаем первый блок
        if not buffer:  # если файл пустой
            print("Файл пустой.\nОтредактируйте файл или добавьте не пустой файл text.txt.\n")
            print("Время работы: ",time.process_time(), "секунд")
        else:
            while buffer:
                s = buffer
                print(s)   #вывод текста из файла
                s = re.sub(r'[^\w\s]', ' ', s)  # удаляем знаки препинания из текста
                words = dict()
                for word in s.split(" "):  # разбиваем строку на слова
                    words[len(word)] = word
                biggestWord = words[max(words)] # находим слово с наибольшим количеством английских символов
                count = len(biggestWord)  # подсчет количества символов в слове
                pozition = buffer.find(biggestWord)  # поиск начального индекса длинного слова
                buffer = f.read(max_buffer_len)   # читаем очередной блок
            print("Самое длинное слово =", biggestWord)
            print("Длина cамого длинного слова в тексте = ", count, "cимволов")
            print("Начальная позиция или первый индекс самого длинного слова:", pozition)
            print("Время работы: ", time.process_time(), "секунд")
except FileNotFoundError:
    print("Файл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    print("Время работы программы: ", time.process_time(), "секунд")
