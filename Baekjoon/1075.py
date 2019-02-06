N = list(input())
F = int(input())
result = ''

for i in range(10):
    N[-2] = '0'
    N[-1] = str(i)
    num = ''

    for n in N:
        num += n
    
    if int(num) % F == 0:
        result = num[-2:]
        break

if result == '':
    for i in range(10,100):
        N[-2], N[-1] = list(str(i))
        num = ''
        for n in N:
            num += n
        
        if int(num) % F == 0:
            result = num[-2:]
            break

print(result)





