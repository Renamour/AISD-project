import random
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + ", промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
        
    K = int(input("Введите число К="))
    start = time.time()
    
    A,F,AT,AF,FT = [],[],[],[],[]                      # задаем матрицы 
    for x in range(row_q):
        A.append([0]*row_q)
        F.append([0]*row_q)
        AT.append([0]*row_q)
        AF.append([0]*row_q)
        FT.append([0]*row_q)
        
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for x in range(row_q):  # заполняем матрицу А
        for y in range(row_q):
            # A[x][y] = random.randint(-10, 10)
            if x < y and y < row_q-1-x:
                A[x][y] = 1
            elif x < y and y > row_q-1-x:
                A[x][y] = 2
            elif x > y and y > row_q-1-y:
                A[x][y] = 3
            elif x > y and y < row_q-1-x:
                A[x][y] = 4

    time_prev = time_next
    time_next = time.time()
    print_matrix(A,"A",time_next-time_prev)

    for x in range(row_q):  # формируем матрицу F
        for y in range(row_q):
            F[x][y] = A[x][y]
            
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    E = []  # задаем матрицу E
    size = row_q // 2
    for x in range(size):
        E.append([0] * size)

    for x in range(size):  # формируем подматрицу E
        for y in range(size):
            E[x][y] = F[x][y]
            
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)


    # сумма чисел, по периметру области 1 в подматрице E

    summa = 0 # сумма чисел
    point = 0
    
    if size % 2 == 0:
        for x in range(size // 2):
            for y in range(size):
                if point == 0:
                    summa += E[x][y]
                elif point != 0 and (y == point or y == size - 1 - point):
                    summa += E[x][y]
            point += 1
    else:
        for x in range(size // 2 + 1):
            for y in range(size):
                if point == 0:
                    summa += E[x][y]
                elif point != 0 and (y == point or y == size - 1 - point):
                    summa += E[x][y]
            point += 1


    # количество нулей, по периметру области 4 в подматрице E

    quantity_zero = 0 # количество нулей
    point = 0

    if size % 2 == 0:
        for y in range(size // 2):
            for x in range(size):
                if point == 0 and x == 0:
                    quantity_zero += 1
                elif point != 0 and x == 0 and(y == point or y == size - 1 - point):
                    quantity_zero += 1
            point += 1
    else:
        for y in range(size // 2 + 1):
            for x in range(size):
                if point == 0 and x == 0:
                    quantity_zero += 1
                elif point != 0 and x == 0 and(y == point or y == size - 1 - point):
                    quantity_zero += 1
            point += 1
    if summa > quantity_zero:
        print("В подматрице E сумма чисел по периметру области 1 больше, чем количество нулей по периметру области 4")
        
        #меняем 1 и 3 области симметрично

        C = []  # задаем матрицу C
        size = row_q // 2
        for x in range(size):
            C.append([0] * size)

        for x in range(size):  # формируем подматрицу C
            for y in range(size):
                C[x][y] = F[size + row_q % 2 + x][size + row_q % 2 + y]
                
        time_prev = time_next
        time_next = time.time()
        print_matrix(C, "C", time_next - time_prev)
        
        point = 0
        
        if size % 2 == 0: 
            for x in range(size // 2):              
                for y in range(size):
                    if y >= point and y <= size - 1 - point:
                        C[x][y], C[size-x-1][size-y-1] = C[size-x-1][size-y-1], C[x][y]
                point += 1
        else:
            for x in range(size // 2 + 1):              
                for y in range(size):
                    if y >= point and y <= size - 1 - point:
                        C[x][y], C[size-x-1][size-y-1] = C[size-x-1][size-y-1], C[x][y]
                point += 1
        for y in range(size):
            for x in range(size):
                F[size + row_q % 2 + x][size + row_q % 2 + y] = C[x][y]
                
        print_matrix(C, "C", time_next - time_prev)                   

    else:                                       
        print("В подматрице E количество нулей по периметру области 4 больше, чем сумма чисел по периметру области 1")
        #меняем матрицы B и E несимметрично      
        for x in range(size):
            for y in range(size):
                F[x][y], F[x][row_q - size + y] = F[x][row_q - size + y], F[x][y]            
    print_matrix(F, "F", time_next - time_prev)
    for x in range(row_q):      # A^T
        for y in range(x,row_q,1):
            AT[x][y],AT[y][x] = A[y][x],A[x][y]
            
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"A^T",time_next-time_prev)

    for x in range(row_q):      # K*A^T
        for y in range(row_q):
            AT[x][y] = K*AT[x][y]
            
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"K*A^T",time_next-time_prev)

    for x in range(row_q):      # (K*A^T)*A
        for y in range(row_q):
            s = 0
            for z in range(row_q):
                s= s + A[x][z] * F[z][y]
            AF[x][y] = s            
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF,"(K*A^T)*A",time_next-time_prev)
    for x in range(row_q):      # F^T
        for y in range(x,row_q,1):
            FT[x][y],FT[y][x] = F[y][x],F[x][y]            
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT,"F^T",time_next-time_prev)

    for x in range(row_q):      # K*F^T
        for y in range(row_q):
            FT[x][y] = K*FT[x][y]
            
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT,"K*F^T",time_next-time_prev)
    for x in range(row_q):      # ((K*A^T)*A)-K*F^T
        for y in range(row_q):
            AF[x][y] = AF[x][y]-FT[x][y]            
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF,"((K*A^T)*A)-K*F^T",time_next-time_prev)    
    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")    
except ValueError:
    print("\nэто не число")                     
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
