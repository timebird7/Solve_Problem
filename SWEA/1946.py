TC = int(input())

for tc in range(TC):
    print('#{}'.format(tc+1))
    N = int(input())
    ans = ''
    for n in range(N):
        tmp = input().split()
        ans += tmp[0]*int(tmp[1])

    for i in range(len(ans)):
        print('{}'.format(ans[i]),end='')
        if i%10 == 9:
            print()
    else:
        print()