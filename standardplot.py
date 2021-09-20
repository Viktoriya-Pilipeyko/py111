
str = input('Введите: ')

print(str.title())

password = input('Введите пароль: ')

recomend = 'Пароль то, что нужно!'
if len(password) < 12:
    recomend = 'количество символов в пароле должно быть 12 и более'
if password.isalnum():
    recomend += ', пароль должен включать и цифры и буквы'
b = 0
a = 0
for l in password:
    upp = l.isupper()
    if upp:
        continue
    else:
        b+=1
for l in password:
    dow = l.islower()
    if dow:
        continue
    else:
        a +=1
if len(password) == b:
    recomend += ', в пароле должны быть заглавные буквы'
if  len(password) == a:
    recomend += ', в пароле должны быть строчные буквы'
if password.find('?') == -1:
        recomend += ', необходим спецсимвол'

print(recomend)
