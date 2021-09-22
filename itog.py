#будем писать прогу для итогового проекта)
#Вам нужно написать программу, которая будет читать файл из предыдущего 
# упражнения, заниматься его чисткой, формировать почтовые адреса для 
# сотрудников, генерировать пароли безопасности для входа в почту, 
# заносить информацию в этот файл и перезаписывать его.

import re
from random import * 

#копируем ф-цию по созданию почты
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


list = [] #итоговый список
listb = [] #список с ошибками
listfmail = [] #список для создания 
file = open('task_file.txt','r') #открываем файл
for line in file: #начинаем перебирать строки
    line = line.replace('\n', '') #убираем перенос(потом добавим вместе с паролем)
    listline = line.split(', ') #делаем список из строки для удобного редактирования
    if re.findall(r' , ', line):
        listb.append(line)
    elif re.findall(r'EMAIL', line):
        listline.append('PASSWORD\n')
        list.append(', '.join(listline))
    elif re.findall(r'[A-Z][a-z]+', listline[1]) and re.findall(r'\d\d\d\d\d\d\d', line):
        #генерим почту
        listfmail = listline[1:3]
        listfmail = email_gen([listfmail])
        print(listfmail)
        listline[0] = listfmail[0]
        #генерим пароль
        i = 1
        password = str(randrange(0,9))
        #начинает собирать пароль:
        for i in range(1,4):
            password += str(randrange(0,9))
            password += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            password += choice('abcdefghijklmnopqrstuvwxyz')
            password += choice('!@#$%^&*()-+')
            i += 4
        listline.append(password)
        #вставляем полученные пароль и почту в список
        list.append(', '.join(listline) + '\n')
    else:
        listb.append(line)
#перезаписываем файл правильными данными
file = open('task_file.txt', 'w+') 
file.write(''.join(list))
file.close     
#создаем новый файл с кривыми данными
bfile = open('bfile.txt', 'w+')
bfile.write(''.join(listb))
bfile.close()
print(list)