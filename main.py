# Project1
"""
Расчёт оптимального объёма потребления двух благ.
Программа:
Проверяет, является ли преполагаемый набор потребления блага X и блага Y оптимальным.
На выходе должны получить оптимальный объем потребления блага X и блага Y при заданом доходе I.


Пользователь вводит с клавиатуры:
p_x - цена блага X для 1кг.
p_y - цена блага Y для 1кг.
I - бюджет потребителя
mu_x - предельная полезность блага X для 1 кг, 2 кг, <...>, n кг, n+1 кг объема потребления блага X.
mu_y - предельная полезность блага Y для 1 кг, 2 кг, <...>, k кг, k+1 кг объема потребления блага Y.
pre_x, pre_y - предполагаемый пользователем оптимальный набор потребления.
"""

x = map(int, input().split())
x = (list(x))
print(x[1])