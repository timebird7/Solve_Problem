def my_sqrt(x):
    n = 1
    m = x
    for t in range(1000):
        k = n+((m-n)/2)
        if k**3 > x:
            m = k
        elif k**3 < x:
            n = k
        else :
            return k
    return (m+n)/2

TC = int(input())

for tc in range(TC):
    N = int(input())

    if int(my_sqrt(N)) - my_sqrt(N) < 0.000000001:
        print(f'{tc+1} {int(my_sqrt(N))}')

    else:
        print(f'{tc+1} -1')