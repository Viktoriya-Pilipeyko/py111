sum = 0
for i in range(10):
    number = int(input('введите числа: '))
    sum += number
print("сумма чисел: " + str(sum))


num_zeroes = 0
for i in range(int(input('количество чисел: '))):
    if int(input()) == 0:
        num_zeroes += 1
print("количество нулей: " + str(num_zeroes))


a = 1
for i in range(int(input('количество ступенек: '))):
    print(a, end = '')
    a +=1

n = int(input('количество ступенек: ')) + 1
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print(*range(1, i), *range(1, i - 1)[::-1], sep='')
