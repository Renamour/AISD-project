import os
import  re
import time
buffer_len = 1  # размер буфера чтения
work_buffer = ""  # рабочий буфер
engl_flag = False  # флаг англ. текста
try:
    with open("test.txt", "r") as file:  # открываем файл
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # читаем первый блок
        if not buffer:  # если файл пустой
            print(
                "\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:  # пока файл не пустой
            if buffer >= 'A' and buffer <= 'Z':  # обрабатываем текущий блок
                engl_flag = True
                work_buffer += buffer.lower() # переводим в нижний регистр символы
            else:
                work_buffer += buffer
                if buffer >= 'a' and buffer <= 'z':
                    engl_flag = True
            if buffer.find(".") >= 0 or buffer.find("!") >= 0 or buffer.find("?") >= 0:  # если символ- окончание предложения
                if engl_flag:
                 print(work_buffer)
                 s = work_buffer
                 s = re.sub(r'[^\w\s]', '', s) #  удаляем знаки препинания из текста
                 s = s.split() # разбиваем строку на слова
                 maxi = max(s, key=len) # находим слово с наибольшим количеством символов
                 count = len(maxi) # подсчет количества символов в слове
                 pozition=work_buffer.find(maxi) # поиск начального индекса длинного слова
                engl_flag = False
                work_buffer = ""
            buffer = file.read(buffer_len)
        print("Время выполнения: " + str(time.process_time()))
        print("Самое длинное слово =", maxi)
        print("Длина длинной последовательности = ", count)
        print("Начальная позиция или индекс самого длинного слова:", pozition)
except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")



