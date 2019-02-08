def my_len(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

TC = int(input())

for tc in range(TC):
    str1 = input()
    str2 = input()

    result = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > result :
            result = cnt

    print(f'#{tc+1} {result}')