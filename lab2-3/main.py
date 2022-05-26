import re
import time
max_buffer_len = 100  # максимальный размер рабочего буфера
buffer_len = 1          # размер буфера чтения
work_buffer = ""        # рабочий буфер
engl_flag = False
try:
    with open("text.txt", "r", encoding="utf-8") as f:  # открываем файл
        buffer = f.read(buffer_len)  # читаем первый блок
        if not buffer:  # если файл пустой
            print("Файл пустой.\nОтредактируйте файл или добавьте не пустой файл text.txt.\n")
        else:
            while buffer and len(work_buffer) < max_buffer_len:
                    if 'a' <= buffer <= 'z' or 'A' <= buffer <= 'Z':
                        work_buffer += buffer
                        engl_flag = True
                    if buffer.find(".") >= 0 or buffer.find("!") >= 0 or buffer.find("?") >= 0:  # Если символ- окончание предложения
                        if engl_flag:  # Если в предложении был английский текст
                            print(work_buffer)
                            s=work_buffer
                            s = re.sub(r'[^\w\s]', ' ', s)
                            words = dict()
                            for word in s.split(" "):
                                words[len(word)] = word
                            biggestWord = words[
                                max(words)]
                            count = len(biggestWord)
                            pozition = buffer.find(biggestWord)
                            print("Самое длинное слово =", biggestWord)
                            print("Длина cамого длинного слова в тексте = ", count, "cимволов")
                            print("Начальная позиция или первый индекс самого длинного слова:", pozition)
                            print("Время работы: ", time.process_time(), "секунд")
                        else:
                            engl_flag = False
                            work_buffer = ""
                    buffer = f.read(max_buffer_len)   # читаем очередной блок
            if len(work_buffer) >= max_buffer_len:
                       print("Превышен максимальный размер буфера\nИзмените файл или добавьте корректный файл в директорию")
except FileNotFoundError:
    print("Файл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    print("Время работы программы: ", time.process_time(), "секунд")
