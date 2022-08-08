
# TASK 1
# Напишите функцию dislike_6(a), которая всегда возвращает True, если только не
# передается число 6 типа int или типа float (в данном случае она вернет «Только
# не 6!»).
#def dislike_6(a):
#    if a == 6:
#        return "Только не 6"
#    else:
#        return True
#
#def dislike_6_ver2(a):
#    if (type(a) is float or type(a) is int) and a == 6.0:
#        return 'Только не 6!'
#    return True
#
#print(dislike_6(6))
#print(dislike_6(7))
#print(dislike_6("6"))
#print(dislike_6(6.0))

# TASK 4
#
#def divider(a, b):
#    if b == 0:
#        return "Нуль в знаменателе"
#    return (a/b)**3
#
#print(divider(10,5))
#print(divider(10,0))

# TASK 1
#my_list = [2, 4, 8]
#print(my_list[::-1])
#
#my_list2 = [1, 2, 3]
#my_list2.reverse()
#print(my_list2)

# tASK 2
# Напишите функцию change(lst), которая принимает список и меняет местами
# его первый и последний элемент. В исходном списке минимум 2 элемента.
#def change(lst):
#
#    buff_first = lst.pop(0)
#    buff_last = lst.pop()
#    print(f"first = {buff_first} last = {buff_last}")
#
#change([1,2,3,4,5,6])

# tASK 3
# Функция to_list() принимает неограниченное количество параметров.
# Обработайте их так, чтобы на выходе получить список из этих элементов.
#def to_list(*args):
#    my_list = []
#    for i in args:
#        my_list.append(i)
#    return my_list
#
#print(to_list('a', 1, 3, 4, "avs"))
# def to_list_2(*args):
#     return list(args)

# Николай задумался о поиске «бесполезного» числа на основании списка.
# Суть оного в следующем: он берет произвольный список чисел, находит самое
# большое из них, а затем делит его на длину списка.
# Студент пока не придумал, где может пригодиться подобное значение, но ищет
# у вас помощи в реализации такой функции useless(s).
def useless(s):
    buff = 0
    for i in s:
        if buff < s[i-1]:
            buff = s[i-1]
    res = buff / s

print(useless([1,3,8,6]))

