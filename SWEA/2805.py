TC = int(input())

for tc in range(TC):
    ans = 0
    N = int(input())
    for i in range(N//2):
        tmp = list(map(int,list(input())))
        ans += sum(tmp[N//2-i:N//2+i+1])

    tmp = list(map(int,list(input())))
    ans += sum(tmp)

    for i in range(N//2):
        tmp = list(map(int,list(input())))
        ans += sum(tmp[i+1:N-1-i])

    print(f'#{tc+1} {ans}')