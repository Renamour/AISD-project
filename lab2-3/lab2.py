import os
import re
max_buffer_len = 100  # максимальный размер рабочего буфера
buffer_len = 1  # размер буфера чтения
work_buffer = ""  # рабочий буфер
engl_flag = False  # флаг англ. текста'

try:
    with open("text.txt", "r") as file:  # открываем файл
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
                print("\n-----Текст из файла-----\n ",work_buffer)
                if engl_flag:  # Если в предложении был английский текст
                    s = work_buffer
                    s= re.sub(r'[^\w\s]+|[\d]+', r'', s).strip()
                    r = " ".join(s.split())
                    print("Обработка и вывод из текста английскую последовательность слов = ", r)
                    r = r.replace(" ", "")
                    k = s.split()
                    res = len(k)
                    print ("Количество слов в последовательности = ",res)

                    l = max(s.split(), key=len)
                    for i in s.split():
                        if len(i) == len(l):
                            qw = r.find(i)
                            print (f"Длинное слово в анг. последовательности = {i}, его количество символов =  {len(i)} и начальная позиция буквы в последовательности = {qw+1}, (считает только буквы без учета пробела, цифр, знаков препинания и др.)")
                else :
                    engl_flag = False
                work_buffer = ""
            buffer = file.read(buffer_len)  # читаем очередной блок
        if len(work_buffer) > 0:  # Если буфер переполнен и нет окончания предложения
            print("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
