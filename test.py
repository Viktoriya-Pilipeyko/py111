n = int(input())

memlist = {}

def facttt(f):
    factorial = 1
    try:
        if memlist[f]:
            print('for key ' + str(f) + 'value ' + str(memlist[f]))
    except:  
        for i in range(2, f+1):
            factorial *= i
            memlist[f] = factorial
        print(str(factorial)+ ' factorial')
print(facttt(n))
print(facttt(n))
print(facttt(n))
print(memlist[n])