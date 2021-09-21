from random import * #импортируем библиотеку
from standardplot import passwordrecom
i = 1
password = str(randrange(0,9))
#начинает собирать пароль:
for i in range(1,4):
    password += str(randrange(0,9))
    password += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    password += choice('abcdefghijklmnopqrstuvwxyz')
    password += choice('!@#$%^&*()-+')
    i += 4
#print(password)
print(passwordrecom(password))

