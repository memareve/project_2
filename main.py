# Project2
"""
Расчёт оптимального объёма потребления двух благ.

Программа:
Проверяет, является ли выбранный набор потребления блага X и блага Y оптимальным.
На выходе должны получить оптимальный объем потребления блага X и блага Y при заданом доходе I.


Пользователь вводит с клавиатуры:
p_x - цена блага X для 1кг.
p_y - цена блага Y для 1кг.
I - бюджет потребителя
mu_x - предельная полезность блага X для 1 кг, 2 кг, <...>, n кг, n+1 кг объема потребления блага X.
mu_y - предельная полезность блага Y для 1 кг, 2 кг, <...>, n кг, n+1 кг объема потребления блага Y.
pre_x, pre_y - выбранный пользователем набор потребления.
"""

mu_y = []
k = 1
I = int(input('Ваш бюджет: '))

p_x = int(input('Цена блага X: '))
p_y = int(input('Цена блага Y: '))

print('Предельная полезность блага X (ввод в строку) в ютилях: ', end='')
mu_x = map(int, input().split())
mu_x = (list(mu_x))

for i in range(len(mu_x)):
    print('Предельная полезность блага Y для ', k, ' кг в ютилях: ', sep='',end='')
    mu_y.append(int(input()))
    k += 1

pre_x, pre_y = map(int, input('Преполагаемый оптимальный набор X кг и Y кг: ').split())

'''
Оптимальный объём потребления блага X и блага Y достигается тогда, 
когда отношение предельных полезностей равно отношению цен этих благ.

А также бюджет (доход) должен быть полностью израсходован.
'''

for i in range(len(mu_x)):
    for j in range(i + 1,len(mu_y) - 1):
        if (mu_x[i] / mu_y[j]) == (p_x/p_y) and (p_x * (i + 1) + p_y * (j + 1) == I):
            true_x, true_y = i + 1, j + 1
if true_x == pre_x and true_y == pre_y:
    print('Выбранный набор', pre_x, 'кг блага X и', pre_y, 'кг блага Y является оптимальным.')
else:
    print('Выбранный набор', pre_x, 'кг блага X и', pre_y, 'кг блага Y не является оптимальным.')
    print('Оптимальный набор:', true_x, 'кг блага X и', true_y, 'кг блага Y')


