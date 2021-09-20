#будет выводить значение по заданному ключу
""" dict = {'Hello' : '', 'Bye' : '', 'List' : ''}
your_input = input('введите для hello: ')
dict['Hello'] = your_input
your_input = input('введите для bye: ')
dict['Bye'] = your_input
your_input = input('введите для List: ')
dict['List'] = your_input
print(dict) """

#Программа должна производить поиск по значению и выдавать ключ
""" dict1 = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
inputvalue = input('Введите значение: ')
for key, value in dict1.items():
    if value == inputvalue:
        print(key)
    else:
        continue
 """
 #принимает список строк и выводит количество повторений данных строк в списке
list = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
dictcount = {i:list.count(i) for i in list}
print (dictcount)