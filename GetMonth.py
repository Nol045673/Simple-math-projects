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
    d = dict() # общий словарь
    girls = dict() # словарь с девочками
    boys = dict() # словарь с мальчиками
    for k in range(len(Datas)): # Перебор месяцев
        ss = Datas[k, 1] # берем дату рождения
        sex = str(Datas[k, 0]) # берем пол
        se = GetMonth(ss) # определяем месяц
        # проверяем если месяц есть в словаре, то прибавляем к месяцу 1, если нет, то добовляем месяц, записывая в его 1
        if se not in d:
            d[se] = 1
            # иероглифы, т.к. файл по какой-то причине выдает битые названия.
            if sex == "Женский":
                if se not in girls:
                    girls[se] = 1
            if sex == "Мужской":
                if se not in boys:
                    boys[se] = 1
        else:
            d[se] += 1
            if sex == "Женский":
                if se in girls:
                    girls[se] += 1
            if sex == "Мужской":
                if se in boys:
                    boys[se] += 1
    return [d, girls, boys] # возвращаем словари

# метод для определения месяца
def GetMonth(data):
    k = data.split('.')
    return int(k[1])


# читаем данные с csv
with open('BirtthStud.csv', 'r', encoding="utf-8") as MyData:
    DatReader = list(csv.reader(MyData, delimiter='\t'))
Datas = np.array(DatReader[1:])
print(len(Datas)) # кол-во строк
# показываем все гистограммы
dictionary, dictionary_girls, dictionary_boys = GeneralNum(Datas)
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
plt.bar(list(dictionary_girls.keys()), dictionary_girls.values(), color='r')
plt.show()
plt.bar(list(dictionary_boys.keys()), dictionary_boys.values(), color='b')
plt.show()
# каждая гистограмма открывается при закрытии предыдущей
