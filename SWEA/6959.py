TC = int(input())

for tc in range(TC):
    num = input()
    cnt = 0
    while True:
        if len(num) > 2:
            num = str(int(num[0]) + int(num[1])) + num[2:]
            cnt += 1
        elif len(num) == 2:
            num = str(int(num[0]) + int(num[1]))
            cnt += 1
        elif len(num) == 1:
            break

    if cnt%2:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} B')
