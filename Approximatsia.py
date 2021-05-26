import csv
import numpy as np
import matplotlib.pyplot as plt

# Задача:
# Аппроксимировать данные по методу наименьших квадратов
# двумя способами: numpy и обычным
# Данные берутся из файла csv такого формата:
# #No     X       Y
# 1       -1      0.236097581
# 2       -0.98   0.250427343
# .......

x_arr = []
y_arr = []
flag = False
with open('1.csv', 'r', encoding="utf-8") as MyData:
    DatReader = list(csv.reader(MyData, delimiter='\t'))
datas = np.array(DatReader[1:])
for i in datas:
    for h in i:
        if not flag:
            print(h)
            flag = True
        x_arr.append(float(h.split()[1]))
        y_arr.append(float(h.split()[2]))


# Через numpy:
def function_numpy():
    x_arr_np = np.array(x_arr)
    y_arr_np = np.array(y_arr)
    t = np.linspace(-1, 1)
    func = np.polyfit(x_arr_np, y_arr_np, 2)
    korni = np.poly1d(func)
    plt.grid()
    plt.plot(x_arr_np, y_arr_np, 'o', t, korni(t), 'b')
    plt.show()


# С использованием уравнений
def function_simple(x, y):
    d = 2  # степень полинома
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, d, full=True)  # Модель
    f = np.poly1d(fp)  # аппроксимирующая функция
    y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
    so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
    print('Average quadratic deviation ' + str(so))
    fx = np.linspace(x[0], x[-1] + 1, len(x))  # можно установить вместо len(x) большее число для интерполяции
    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(fx, f(fx), linewidth=2)
    plt.grid(True)
    plt.show()


function_simple(x_arr, y_arr)
function_numpy()
