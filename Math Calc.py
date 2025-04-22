from math import pi, sqrt, sin
from sympy.solvers import solve
from sympy.abc import x, y, z
from sympy import Matrix, Symbol, solve_linear_system
import pprint


def sec_num(lst, num):
    for i in lst:
        if num.isdigit() and num in i[0]:
            return True
            break
    else:
        print('Введите число, доступное в списке!')


def sec_val(val):
    if '.' not in val and val.isdigit():
        return True
    else:
        if val.count('.') == 1 and val[0] != '.' and val[-1] != '.':
            val = val.replace('.', '')
            if val.isdigit():
                return True
            else:
                print('Введите верное десятичное число!')
        else:
            print('Введите число!')


def sec_opr(opr):
    if len(opr) == 1 and not opr.isdigit() and not opr.isalpha():
        if opr == '+' or opr == '-' or opr == '*':
            return True
        elif opr == '/':
            print('Деление не поддерживается. Используйте другой оператор.')
        else:
            print('Введите доступные операторы "+, -, *"')
    else:
        print('Введите оператор вычисления!')


def sec_opr_lu(opr):
    if len(opr) == 1 and not opr.isdigit() and not opr.isalpha():
        if opr == '+' or opr == '-' or opr == '*':
            return True
        elif opr == '/' or opr == '*':
            print('Деление и умножение, не используются. Используйте другой оператор.')
        else:
            print('Введите доступные операторы "+, -"')
    else:
        print('Введите оператор вычисления!')


class Geometry():
    def sq_area(self):
        print('Введите длину стороны квадрата: ')
        while True:
            len_side = input()
            if sec_val(len_side) == True:
                len_side = float(len_side)
                break
        print(f'Площадь квадрата равна: {len_side ** 2}')

    def sq_circ(self):
        src_met = ['1. По радиусу', '2. По диаметру', '3. По длине окружности']
        print('Выберите способ поиска площади:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        if met == 1:
            print('Введите радиус круга: ')
            while True:
                rad = input()
                if sec_val(rad) == True:
                    rad = float(rad)
                    break
            print(f'Площадь круга равна: {pi * (rad ** 2):.3f}')
        elif met == 2:
            print('Введите диаметр круга: ')
            while True:
                dmt = input()
                if sec_val(dmt) == True:
                    dmt = float(dmt)
                    break
            print(f'Площадь круга равна: {(dmt ** 2) / 4 * pi:.3f}')
        elif met == 3:
            print('Введите длину окружности: ')
            while True:
                leng = input()
                if sec_val(leng) == True:
                    leng = float(leng)
                    break
            print(f'Площадь круга равна: {(leng ** 2) / (4 * pi):.3f}')

    def sq_triang(self):
        src_met = ['1. По основанию и высоте', '2. По длинам сторон и полупериметру',
                   '3. По двум сторонам и углу между ними',
                   '4. Через радиус вписанной окружности и длины сторон',
                   '5. Через радиус описанной окружности и длины сторон']
        print('Выберите способ поиска площади:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        if met == 1:
            print('Введите длину основания: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите высоту: ')
            while True:
                h = input()
                if sec_val(h) == True:
                    h = float(h)
                    break
            print(f'Площадь треугольника равна: {a * h / 2}')
        elif met == 2:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину стороны b: ')
            while True:
                b = input()
                if sec_val(b) == True:
                    b = float(b)
                    break
            print('Введите длину стороны c: ')
            while True:
                c = input()
                if sec_val(c) == True:
                    c = float(c)
                    break
            p = (a + b + c) / 2
            print(f'Площадь треугольника равна: {sqrt(p * (p - a) * (p - b) * (p - c))}')
        elif met == 3:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину стороны b: ')
            while True:
                b = input()
                if sec_val(b) == True:
                    b = float(b)
                    break
            print('Введите угол между ними: ')
            while True:
                alph = input()
                if sec_val(alph) == True:
                    alph = float(alph)
                    break
            print(f'Площадь треугольника равна: {(a * b * sin(alph)) / 2}')
        elif met == 4:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину стороны b: ')
            while True:
                b = input()
                if sec_val(b) == True:
                    b = float(b)
                    break
            print('Введите длину стороны c: ')
            while True:
                c = input()
                if sec_val(c) == True:
                    c = float(c)
                    break
            print('Введите радиус окружности: ')
            while True:
                r = input()
                if sec_val(r) == True:
                    r = float(r)
                    break
            print(f'Площадь треугольника равна: {r * (a + b + c) / 2}')
        elif met == 5:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину стороны b: ')
            while True:
                b = input()
                if sec_val(b) == True:
                    b = float(b)
                    break
            print('Введите длину стороны c: ')
            while True:
                c = input()
                if sec_val(c) == True:
                    c = float(c)
                    break
            print('Введите радиус окружности: ')
            while True:
                r = input()
                if sec_val(r) == True:
                    r = float(r)
                    break
            print(f'Площадь треугольника равна: {(a * b * c) / (4 * r)}')

    def sq_rect(self):
        src_met = ['1. По длине и ширине', '2. По диагоналям и синусу угла между ними',
                   '3. По стороне и диагонали', '4. По периметру и стороне']
        print('Выберите способ поиска площади:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        if met == 1:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину стороны b: ')
            while True:
                b = input()
                if sec_val(b) == True:
                    b = float(b)
                    break
            print(f'Площадь прямоугольника равна: {a * b}')
        elif met == 2:
            print('Введите длину диагонали: ')
            while True:
                d = input()
                if sec_val(d) == True:
                    d = float(d)
                    break
            print('Введите угол между диагоналями: ')
            while True:
                alph = input()
                if sec_val(alph) == True:
                    alph = float(alph)
                    break
            print(f'Площадь прямоугольника равна: {((d ** 2) * sin(alph)) / 2}')
        elif met == 3:
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print('Введите длину диагонали: ')
            while True:
                d = input()
                if sec_val(d) == True:
                    d = float(d)
                    break
            print(f'Площадь прямоугольника равна: {a * sqrt((d ** 2) - (a ** 2))}')
        elif met == 4:
            print('Введите периметр прямоугольника: ')
            while True:
                p = input()
                if sec_val(p) == True:
                    p = float(p)
                    break
            print('Введите длину стороны a: ')
            while True:
                a = input()
                if sec_val(a) == True:
                    a = float(a)
                    break
            print(f'Площадь прямоугольника равна: {p * a - 2 * a}')


class Algebra():
    def mtrx(self):
        src_met = ['1. 2x2', '2. 3x3', '3. 4x4']
        print('Выберите размер матрицы:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        matrix1 = []
        matrix2 = []
        if met == 1:
            matrix1 = Matrix(
                [[float(input(f'Первая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(2)]
                 for i in range(2)])
            matrix2 = Matrix(
                [[float(input(f'Вторая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(2)]
                 for i in range(2)])
            print('Введите символ требуемой операции: ')
            while True:
                opr = input()
                if sec_opr(opr) == True:
                    break
            match opr:
                case '+':
                    matrix_res = matrix1 + matrix2
                case '-':
                    matrix_res = matrix1 - matrix2
                case '*':
                    matrix_res = matrix1 * matrix2
            pp = pprint.PrettyPrinter()
            pp.pprint(matrix_res)
        elif met == 2:
            matrix1 = Matrix(
                [[float(input(f'Первая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(3)]
                 for i in range(3)])
            matrix2 = Matrix(
                [[float(input(f'Вторая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(3)]
                 for i in range(3)])
            print('Введите символ требуемой операции: ')
            while True:
                opr = input()
                if sec_opr(opr) == True:
                    break
            match opr:
                case '+':
                    matrix_res = matrix1 + matrix2
                case '-':
                    matrix_res = matrix1 - matrix2
                case '*':
                    matrix_res = matrix1 * matrix2
            pp = pprint.PrettyPrinter()
            pp.pprint(matrix_res)
        elif met == 3:
            matrix1 = Matrix(
                [[float(input(f'Первая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(4)]
                 for i in range(4)])
            matrix2 = Matrix(
                [[float(input(f'Вторая матрица:\nВведите число {j + 1} для строки {i + 1}: ')) for j in range(4)]
                 for i in range(4)])
            print('Введите символ требуемой операции: ')
            while True:
                opr = input()
                if sec_opr(opr) == True:
                    break
            match opr:
                case '+':
                    matrix_res = matrix1 + matrix2
                case '-':
                    matrix_res = matrix1 - matrix2
                case '*':
                    matrix_res = matrix1 * matrix2
            pp = pprint.PrettyPrinter()
            pp.pprint(matrix_res)

    def mtrx_tr(self):
        src_met = ['1. 2x2', '2. 3x3', '3. 4x4']
        print('Выберите размер матрицы:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        matrix1 = []
        match met:
            case 1:
                matrix1 = Matrix(
                    [[float(input(f'Введите число {j + 1} для строки {i + 1}: ')) for j in range(2)]
                     for i in range(2)])
                pp = pprint.PrettyPrinter()
                pp.pprint(matrix1.T)
            case 2:
                matrix1 = Matrix(
                    [[float(input(f'Введите число {j + 1} для строки {i + 1}: ')) for j in range(3)]
                     for i in range(3)])
                pp = pprint.PrettyPrinter()
                pp.pprint(matrix1.T)
            case 3:
                matrix1 = Matrix(
                    [[float(input(f'Введите число {j + 1} для строки {i + 1}: ')) for j in range(4)]
                     for i in range(4)])
                pp = pprint.PrettyPrinter()
                pp.pprint(matrix1.T)

    def func_alg(self):
        src_met = ['1. С двумя переменными', '2. С тремя переменными']
        print('Выберите нужную систему:', *src_met, sep='\n')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break
        system = []
        if met == 1:
            system = Matrix(
                [[float(input(f'Введите число {j + 1} для строки {i + 1}: ')) for j in range(3)]
                 for i in range(2)])
            print(solve_linear_system(system, x, y))
        elif met == 2:
            system = Matrix(
                [[float(input(f'Введите число {j + 1} для строки {i + 1}: ')) for j in range(4)]
                 for i in range(3)])
            print(solve_linear_system(system, x, y, z))

    def disc(self):
        src_met = ['1. Обычное уравнение', '2. Квадратное уравнение', '3. Биквадратное уравнение']
        print('Выберите способ решения:', *src_met, sep='\n')
        x = Symbol('x')
        while True:
            met = input()
            if sec_num(src_met, met) == True:
                met = int(met)
                break

        print('Введите число a: ')
        while True:
            a = input()
            if sec_val(a) == True:
                a = float(a)
                break
        print('Введите число b: ')
        while True:
            b = input()
            if sec_val(b) == True:
                b = float(b)
                break

        if met != 1:
            print('Введите число c: ')
            while True:
                c = input()
                if sec_val(c) == True:
                    c = float(c)
                    break

        print('Введите первый оператор выисления: ')
        while True:
            opr1 = input()
            if sec_opr_lu(opr1) == True:
                break

        if met != 1:
            print('Введите второй оператор высиления: ')
            while True:
                opr2 = input()
                if sec_opr_lu(opr2) == True:
                    break

        match met:
            case 1:
                if opr1 == '+':
                    print(f'Иксы равны: {solve(a * x + b)}')
                else:
                    print(f'Иксы равны: {solve(a * x - b)}')
            case 2:
                if opr1 == opr2:
                    if opr1 == '+':
                        print(f'Иксы равны: {solve(a * x ** 2 + b * x + c)}')
                    else:
                        print(f'Иксы равны: {solve(a * x ** 2 - b * x - c)}')
                else:
                    if opr1 == '+' and opr2 == '-':
                        print(f'Иксы равны: {solve(a * x ** 2 + b * x - c)}')
                    if opr1 == '-' and opr2 == '+':
                        print(f'Иксы равны: {solve(a * x ** 2 - b * x + c)}')
            case 3:
                if opr1 == opr2:
                    if opr1 == '+':
                        print(f'Иксы равны: {solve(a * x ** 4 + b * x ** 2 + c)}')
                    else:
                        print(f'Иксы равны: {solve(a * x ** 4 - b * x ** 2 - c)}')
                else:
                    if opr1 == '+' and opr2 == '-':
                        print(f'Иксы равны: {solve(a * x ** 4 + b * x ** 2 - c)}')
                    if opr1 == '-' and opr2 == '+':
                        print(f'Иксы равны: {solve(a * x ** 4 - b * x ** 2 + c)}')


def sect_geo():
    func_geo = ['1. Площадь квадрата', '2. Площадь круга', '3. Площадь треугольника',
                '4. Площадь прямоугольника']
    geo_act = {'1': Geometry.sq_area, '2': Geometry.sq_circ, '3': Geometry.sq_triang,
               '4': Geometry.sq_rect}
    print('Выберите что требуется посчитать:', *func_geo, sep='\n')
    while True:
        num = input()
        if sec_num(func_geo, num) == True:
            geo_act[num](self=Geometry)
            break


def sect_alg():
    func_alg = ['1. Операции с матрицами. Сумма, разность, произведение.', '2. Транспонирование матрицы.',
                '3. Решение систем',
                '4. Решение линейного уравнения']
    alg_act = {'1': Algebra.mtrx, '2': Algebra.mtrx_tr, '3': Algebra.func_alg,
               '4': Algebra.disc}
    print('Выберите раздел:', *func_alg, sep='\n')
    while True:
        num = input()
        if sec_num(func_alg, num) == True:
            alg_act[num](self=Algebra)
            break


reg = ['1. Геометрия', '2. Алгебра']
print('Введите номер раздела, который вам нужен:', *reg, sep='\n')
while True:
    num = input()
    if sec_num(reg, num) == True:
        match num:
            case '1':
                sect_geo()
                break
            case '2':
                sect_alg()
                break
