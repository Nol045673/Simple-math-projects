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


# Метод для перебора месяцев и записывания их в словари
def GeneralNum(Datas):
    d = dict()  # общий словарь
    girls = dict()  # словарь с девочками
    boys = dict()  # словарь с мальчиками
    for k in range(len(Datas)):  # Перебор месяцев
        ss = Datas[k, 1]  # берем дату рождения
        sex = str(Datas[k, 0])  # берем пол
        se = GetMonth(ss)  # определяем месяц
        # проверяем если месяц есть в словаре, то прибавляем к месяцу 1, если нет, то добовляем месяц, записывая в его 1
        if se not in d:
            d[se] = 1
        else:
            d[se] += 1
        if sex == "Женский":
            if se not in girls:
                girls[se] = 1
            else:
                girls[se] += 1
        if sex == "Мужской":
            if se not in boys:
                boys[se] = 1
            else:
                boys[se] += 1

    return [d, girls, boys]  # возвращаем словари


# метод для определения месяца
def GetMonth(data):
    k = data.split('.')
    return int(k[1])


# читаем данные с csv
with open('BirtthStud.csv', 'r', encoding="utf-8") as MyData:
    DatReader = list(csv.reader(MyData, delimiter='\t'))
Datas = np.array(DatReader[1:])
print(len(Datas))  # кол-во строк
mounth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # месяцы
# показываем все гистограммы
dictionary, dictionary_girls, dictionary_boys = GeneralNum(Datas)
# составим списки:
axes1 = list(dictionary.values())
axes2 = list(dictionary_girls.values())
axes3 = list(dictionary_boys.values())
# покажем каждую
plt.bar(mounth, axes1, color='g', label='Общая')
plt.bar(mounth, axes2, color='r', label='Девочки')
plt.bar(mounth, axes3, color='b', label='Мальчики')
# назвние по y
plt.ylabel('Родилось человек в месяц')
# название по x
plt.xlabel('Месяцы')
# выводим легенду
plt.legend()
plt.show()
