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
    girls = dict()
    boys = dict()
    for k in range(len(Datas)):
        ss = Datas[k, 1]
        sex = str(Datas[k, 0])
        se = GetMonth(ss)
        if se not in d:
            d[se] = 1
            # иероглифы, т.к. файл по какой-то причине выдает битые названия.
            if sex == "Р–РµРЅСЃРєРёР№":  # Женский
                if se not in girls:
                    girls[se] = 1
            if sex == "РњСѓР¶СЃРєРѕР№":  # Мужской
                if se not in boys:
                    boys[se] = 1
        else:
            d[se] += 1
            if sex == "Р–РµРЅСЃРєРёР№":
                if se in girls:
                    girls[se] += 1
            if sex == "РњСѓР¶СЃРєРѕР№":
                if se in boys:
                    boys[se] += 1
    return [d, girls, boys]


def GetMonth(data):
    k = data.split('.')
    return int(k[1])


with open('BirtthStud.csv', 'r') as MyData:
    DatReader = list(csv.reader(MyData, delimiter='\t'))
Datas = np.array(DatReader[1:])
print(len(Datas))

dictionary, dictionary_girls, dictionary_boys = GeneralNum(Datas)
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()
plt.bar(list(dictionary_girls.keys()), dictionary_girls.values(), color='r')
plt.show()
plt.bar(list(dictionary_boys.keys()), dictionary_boys.values(), color='b')
plt.show()
# каждая гистограмма открывается при закрытии предыдущей
