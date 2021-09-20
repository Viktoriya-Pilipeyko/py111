str = 'Abraсadabra'
print(str[2])
print(str[len(str) -2])
print(str[:5])
print(str[:len(str) -2])

for i in range(len(str)):
    if i % 2 == 0:
        continue
    else:
        print(str[i], end='')

print('')

for i in range(len(str)):
    if i % 2 != 0:
        continue
    else:
        print(str[i], end='')
print('')

count = len(str)
for i in range(len(str)):
    print(str[count-1], end='')
    count -=1
print('')

count = len(str)
for i in range(len(str)):
    if i % 2 != 0:
        continue
    else:
        print(str[count-1], end='')
    count -=2
print('')

print(len(str))
