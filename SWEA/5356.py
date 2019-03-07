TC = int(input())

for tc in range(TC):
    words = [[] for i in range(5)]

    for i in range(5):
        words[i] = list(input())

    ans = ''

    for i in range(15):
        for j in range(15):
            try:
                ans += words[j][i]
            except IndexError:
                pass

    print('#{} {}'.format(tc+1,ans))