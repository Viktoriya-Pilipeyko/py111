 #рисуем декортаор
def decoration(func): 
    print('начинаем') #кладем что-то в начало
    def env(*args, **kwargs): #оболочка
        func(*args, **kwargs) #вызываем основную ф-цию
        print('заканчиваем') #кладем что-то в конец
        return func 
    return env

@decoration #вызываем этот декоратор
def test (arg1, *args): #какую ф-цию оборачиваем в декоратор
    print(f"{arg1}")
    for i in args:
        print(i)
test('аргумент один', 10, 15,20) #вызываем ф-цию
