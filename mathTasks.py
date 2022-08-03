from sys import getsizeof

# Task 2
#a = getsizeof(3**9090001)
#b = a/1024
#c = b/1024
#print(f"Bytes = {a}\n Kilobytes = {b}\n Megabytes = {c}")

# Task 3
#print(4**(4**4))

# Task 5
#def pos_add(a,b):
#    return abs(a+b)
#
#print(pos_add(-5,-10))

# Task 7
#a = 5.4
#def num_sum(a):
#    if isinstance(a, int) and not isinstance(a, bool):
#        a_to_str = str(abs(a))
#        s = 0
#        for i in a_to_str:
#            s += int(i)
#        return s
#    return 'Это не целое число'
#
#print(num_sum(-146))
#print(num_sum('-11'))
#print(num_sum(True))

# Task 8
# Дана последовательность случайных цифр любой длины и «волшебное» положительное число, больше нуля.
# Напишите функцию magic(), принимающую эти аргументы, и выясните, можно ли разделить сумму квадратов
# последовательности на «волшебное» число без остатка.
# В качестве ответа возвращается «Волшебство случается» в случае успеха или «Никакого волшебства»,
# если разделить нельзя.
#def magic(*args, k):
#    sq_sum = 0
#    for i in args:
#        sq_sum += i ** 2
#
#    if sq_sum % k == 0:
#        return 'Волшебство случается'
#    return 'Никакого волшебства'
#
#print(magic(2, 5, 7, k=5))
#print(magic(2, 5, 7, k=39))
#print(magic(2, 5, 7, k=2))

# Task 2.1
# Напишите функцию to_float(num), которая преобразует любое число в число с плавающей точкой.
# Если в качестве аргумента передан другой тип данных, она возвращает «Невозможно преобразовать».
#def to_float(num):
#    if isinstance(num, (int, float)):
#        return float(num)
#    return "Невозможно преобразовать"
#print(to_float(12))
#print(to_float(-1.762))
#print(to_float(True))
#print(to_float('Не число'))
#print(to_float('2.2'))

# Task 2.2
# Дано 4 числа. Нужно написать функцию avg_5(a, b, c, d), которая возвращает среднее
# арифметическое аргументов и округляет его до 5 знаков после запятой.
#def avg_5(a, b, c, d):
#    avg = (a+b+c+d)/4
#    return round(avg, 5)
#
#print(avg_5(1, 6, 7, 4))
#print(avg_5(1.7, 6.2, 2, 6))
#print(avg_5(3, -3.143223442, -4.76, 1.3902))

#a = 15
#b = 4
#c = a/b
#c1= a%b
#c2= a//b
#a_total = c1*b + c2
#print(f"c={c}, c%={c1}, c//={c2}, b*целое число + остаток = {a_total} ")

# Task 2.5
# Напишите функцию округления round_standard(num), принимающую число с плавающей точкой
# и округляющую его до целого числа в соответствии с правилами школьной математики.
#def round_standard(num):
#    if num >= 0:
#        sign = 1
#    else:
#        sign = -1
#    return sign * int((abs(num) + 0.5))
#
## Тесты
#print(round_standard(1.5))
#print(round_standard(-2.5))
#print(round_standard(1.6))
#print(round_standard(5.11))

#for i in range(0, 11, 3):
#    print(i)

