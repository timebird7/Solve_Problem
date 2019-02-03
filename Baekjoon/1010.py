from math import factorial

TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))

    result = int(factorial(M)/(factorial(N)*factorial(M-N)))

    print(result)

