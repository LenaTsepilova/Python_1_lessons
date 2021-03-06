# Цепилова ЕВ +
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

my_list = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(my_list)):
    print(i + 1, ".", '{:>7}'.format(my_list[i]), sep="")

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.

A = [1, 2, 3, 4, 7]
B = [1, 2, 5, 6, 7]
i = 0
while i < len(A):
    if A[i] in B:
        del A[i]
        continue
    i += 1
print(A)
        

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

A = [0, 1, 2, 3, 4, 5]
for i in range(len(A)):
    if A[i] % 2 == 0:
        A[i] /= 4
    else:
        A[i] *= 2
print(A)