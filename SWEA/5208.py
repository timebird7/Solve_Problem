TC = int(input())

for tc in range(1,TC+1):
    nums = list(map(int, input().split()))
    cnt = 0

    i = 1
    batt = nums[1]
    while i+batt < nums[0]:
        i += batt

        for j in range(i,i-batt,-1):          
            if j+nums[j] == max([x + y for x, y in zip([k for k in range(i-batt+1,i+1)], nums[i-batt+1:i+1])]):
                batt = nums[j]
                i = j
                cnt += 1
                break

    print(f'#{tc} {cnt}')
