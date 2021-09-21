def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

list = []
list2 = []
list4 = []
list5 = []
list6 = []
file = open('task_file.txt', 'r')
for line in file:
    #сплитуем файл на строки, создавая список
    list.append(line.split(', '))
    #print(list)
for l in list:
    #проверяем строки на соответствие, и создаем список из имен сотрудников
    if l[1] != '' and l[2] != '' and len(l[3]) >= 7 and l[1].istitle() and l[1] != 'NO_NAME':
        list2.append(l[1:3])
#вызываем ф-цию по созданию адресов почты
list3 = (email_gen(list2))

#вновь открываем файл
file = open('task_file.txt', 'r')
for ll in file:
    #заменяем пустое поле с почтой на получившийся адрес:
    lll = ll.split(', ') #создаем строку с элементоми из строчки файла
    for s in list3:
        #перебираем получившиеся адреса
        str = (s.split('.')) #сплитуем фамилию сотрдуника из адреса почты
        if str[0] == lll[2]: #если фамилия из почты равна фамилии сотрудника их списка
            lll[0] = s #меняем пустой элемент почты на адрес почты
        else:
            continue
    list4.append(lll) #созлаем список с заполненным полем почты

for n in list4:
    #соединяем списки внутри списка
    if n[0] == 'EMAIL':
        list5.append(' '.join(n)) #заголовки разделяем пробелами
    else:
        list5.append(', '.join(n)) #элементы разделяем запятыми
list6.append(''.join(list5)) #формируем список из соединенных списков
print(' '.join(list6)) #соединяем готовый список в строку

#обновляем файл
file = open('task_file.txt', 'w')
file.write(''.join(list6))
file.close