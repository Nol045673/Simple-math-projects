import csv
import numpy as np
import matplotlib.pyplot as plt

# Задача:
# Создать статистику рождаемости по месяца.
# Построить гистограммы рождаемости по месяцам.(Общую, мальчиков, девочек)
# Данные берутся из файла csv такого формата:
# #Пол	Дата рождения
# Женский	17.05.1988
# Женский	31.05.1997

def GeneralNum(Datas):
    d = dict()
    for k in range(len(Datas)):
        ss = Datas[k, 1]
        se = GetMonth(ss)
        if se not in d:
            d[se] = 1
        else:
            d[se] += 1
    return d


def GetMonth(data):
    k = data.split('.')
    return int(k[1])


with open('BirtthStud.csv', 'r') as MyData:
    DatReader = list(csv.reader(MyData, delimiter='\t'))
Datas = np.array(DatReader[1:])
print(len(Datas))

dictionary = GeneralNum(Datas)
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
