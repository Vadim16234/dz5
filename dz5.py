# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
print('ЗАДАЧА 26')
z = int(input('Введите первое число для первой задачи: '))
x = int(input('Введите второе число для первой задачи: '))

def show(q, w): # Создал рекурсивную функцию, которая вызывает сама себя
    return q ** w # Первое число возвел в степень, равную второму числу и вернул его

show(z, x) # обратился к функции и поместил в нее значения, введенные пользователем
print('Результат возведения в степень =', show(z, x)) # вывел готовое решение функции



# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

print('ЗАДАЧА 28')

d = int(input('Введите первое число для второй задачи: '))
s = int(input('Введите второе число для второй задачи: '))

def sum(a, b): # Создал рекурсивную функцию
    a += 1 # применил допущенные арифметические операции 'a = a + 1'
    b -= 1 # применил допущенные арифметические операции 'b = b - 1'
    if a >= 0 and b >= 0: # условие проверяет, чтоб число было положительным
        return a + b # вернул результат решения

sum(d, s) # обратился к функции. Можно и без этого, сразу 'print'. 
print('Сумма чисел =', sum(d, s)) # вывел готовый результат решения
