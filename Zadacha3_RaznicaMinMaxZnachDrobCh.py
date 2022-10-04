import math

def fractional_part(*args):
    listDrob = []
    for i in range(len(list)):
        listDrob.append(round(list[i] % 1, 2))
    return listDrob

def find_difference(listDrob):
    sortedList = sorted(listDrob)
    maxElem = sortedList[-1]
    minElem = sortedList[0]
    result = round((maxElem - minElem), 2)
    return result

list = [1.1, 1.2, 3.1, 10.01]
print('Список элементов: ', list)
listDrob = fractional_part(list)
result = find_difference(listDrob)
print(f'Разница между макс и мин знач дробной части элементов: {result}')