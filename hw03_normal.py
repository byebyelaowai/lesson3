# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter1(arg,arg1):
    insideFunction = []

    for a in arg1:
        if a != arg:
            insideFunction.append(a)
# добавляет элемент в конец списка
    return insideFunction
print(filter1(1,[1,2,3,4,2,1,5,6,7,1,8,9,1,5]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a, b, c ,d):
    prllgrm = ""

    if int(a[0]) - int(b[0]) == int(c[0]) - int(d[0]) and int(a[1]) - int(b[1]) == int(c[1]) - int(d[1]):
        prllgrm = ("Это вершины параллелограма")

    else:
        prllgrm = ("Это не вершины параллелограма")

    return prllgrm
print(parallelogram([1,1],[2,2],[3,3],[4,4]))
print(parallelogram([3,1],[3,2],[3,3],[9,4]))