#все элементы списка с четными индексами в виде нового списка.
""" list = (input('Введите список: ').split(','))

for l in range(len(list)):
    if l % 2 != 0:
        continue
    else:
        print(list[l], end=' ')
 """
#все элементы списка, которые больше предыдущего, в виде отдельного списка
""" list = (input('Введите список: ').split(','))

for l in range(len(list)):
    if l > 0:
        if int(list[l]) > int(list[l-1]):
            print(list[l], end=' ')
        else:
            continue
    else:
        continue """
        
#меняет местами наибольший и наименьший элемент и выводит новый список
""" list = (input('Введите список: ').split(','))
maxindex = list.index(max(list, key=lambda i: int(i)))
minindex = list.index(min(list, key=lambda i: int(i)))
maxnum = max(list, key=lambda i: int(i))
minnum = min(list, key=lambda i: int(i))
list[maxindex] = minnum
list[minindex] = maxnum
print(list) """

