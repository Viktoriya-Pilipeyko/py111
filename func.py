#Напишите программу, которая принимает арифметическое выражение в 
# качестве аргумента и выводит результат этого выражения.
def math(str):
    for i in str:
        if i == ' ':
            str = str.replace(' ','')
        if i in '+':
            var = str.split('+')
            print (int(var[0]) + int(var[1]))
        elif i in '-':
            var = str.split('-')
            print (int(var[0]) - int(var[1]))
        elif i in '/':
            var = str.split('/')
            print (int(var[0]) / int(var[1]))
        elif i in '*' and '**' not in str:
            var = str.split('*')
            print (int(var[0]) * int(var[1]))
        elif i in '%':
            var = str.split('%')
            print (int(var[0]) / 100)
        elif i in '**':
            var = str.split('**')
            if var[1] == '':
                print(int(var[0])**2)
            else:    
                print (int(var[0]) ** int(var[1]))

math('4**4')