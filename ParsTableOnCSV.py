import csv
import numpy

all_x = []
with open('vsr08.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for index, row in enumerate(reader, ):
        if index > 0:
            all_x.append(float(row[1]))

print(min(all_x))
print(numpy.mean(all_x))
print(max(all_x))
print(numpy.median(all_x))
print(numpy.var(all_x))
print(numpy.std(all_x))







