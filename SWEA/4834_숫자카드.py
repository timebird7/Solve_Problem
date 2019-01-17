T = int(input())

for x in range(T):
    a = int(input())
    b = list(map(int, list(input())))
    result = sorted(sorted(b), key=b.count)[-1]
    print(f'#{x+1} {result} {b.count(result)}')

