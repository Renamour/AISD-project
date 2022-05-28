import os
import re
max_buffer_len = 100  # максимальный размер рабочего буфера
buffer_len = 1  # размер буфера чтения
work_buffer = ""  # рабочий буфер
engl_flag = False  # флаг англ. текста
try:
    with open("text1.txt", "r") as file:  # открываем файл
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # читаем первый блок
        if not buffer:  # если файл пустой
            print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:  # пока файл не пустой
            if buffer >= 'a' and buffer <= 'z':  # обрабатываем текущий блок
                engl_flag = True
                work_buffer += buffer
            else:
                work_buffer += buffer
                if buffer >= 'A' and buffer <= 'Z':
                    engl_flag = True
            if len(work_buffer) >= max_buffer_len and buffer.find(" ") >= 0 or buffer.find(".")>= 0 or buffer.find("!") >= 0 or buffer.find("?") >= 0:
                print(work_buffer)
                if engl_flag:  # Если в предложении был английский текст
                    s = work_buffer
                    s= re.sub(r'[^\w\s]+|[\d]+', r'', s).strip()
                    words = dict()
                    for word in s.split(" "):  # разбиваем строку на слова
                        words[len(word)] = word
                    biggestWord = words[max(words)]  # находим слово с наибольшим количеством английских символов
                    count = len(words[max(words)])  # подсчет количества символов в слове
                    pozition = work_buffer.find(biggestWord)  # поиск начального индекса длинного слова
                    print("Самое длинное слово =", biggestWord)
                    print("Длина cамого длинного слова в тексте = ", count, "cимволов")
                    print("Начальная позиция самого длинного слова:", pozition+1)
                else :
                    engl_flag = False
                work_buffer = ""
            buffer = file.read(buffer_len)  # читаем очередной блок
        if len(work_buffer) > 0:  # Если буфер переполнен и нет окончания предложения
            print("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
