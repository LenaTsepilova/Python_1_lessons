
__author__ = 'Цепилова ЕВ'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

number = input('введите целое число: ')
for elem in number:
    print(elem)
   

# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input("Введите, два числа. Первое число:"))
b = int(input("Введите, два числа. Второе число:"))
a, b = b, a
print(b)
print(a)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


access = 18
user_access = int(input("Введите Ваш возраст:"))
if user_access >=18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
