TC = int(input())

for tc in range(TC):
    n = float(input())
    ans = ''
    while True:
        n *= 2
        ans += str(int(n))
        n -= int(n)

        if len(ans) > 13:
            ans = 'overflow'
            break

        if n == 0:
            break

    print(f'#{tc+1} {ans}')
