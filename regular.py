import re
#print(re.findall(r'h..', 'hey Hey Hey Hey'))

#print(re.findall(r'\S', 'hey Hey Hey Hey'))
#print(re.findall(r'\b\W', 'hey, Hey1, Hey2, Hey3'))
#print(re.findall(r'.y.', 'hey. Hey1. Hey2. Hey3'))
#print(re.findall(r'\W{1}', 'hey. Hey1. Hey2. Hey3'))
#print(re.findall(r'ey|\w', 'hey. Hey1. Hey2. Hey3'))
#print(re.findall(r'(\w\w\W)', 'hey. Hey1. Hey2. Hey3\n'))
#объявляем список с логами
log = ['Oct 17 01:29:51 legacy sshd[60387]: Illegal user test from 218.237.4.57', 'Oct 17 23:29:11 legacy sshd[64098]: Did not receive identification string from 147.46.76.225 ','Oct 17 23:37:18 legacy sshd[64139]: Illegal user patrick from 147.46.76.225 ','Oct 17 23:37:22 legacy sshd[64141]: Illegal user patrick from 147.46.76.225 ']
#print (log)
for sting in log:
    #перебираем элементы, смотрим есть ли нужные значения
    if re.findall(r'Did',sting): 
        #если находим нужные значения, отбраем ip адрес
        print(re.findall(r'\d+\.\d+\.\d+\.\d+', sting))