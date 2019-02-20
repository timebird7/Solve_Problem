for tc in range(10):
    a = input()
    cnt = 0

    nums = [[0 for x in range(100)] for y in range(100)]

    for i in range(100):
        nums[i] = list(map(int, input().split()))

    for x in range(100):
        for y in range(100):
            if x < y:
                nums[x][y], nums[y][x] = nums[y][x], nums[x][y]

    for i in range(100):
        for j in range(99):
            if nums[i][j] == 1 and 2 in nums[i][j+1:]:
                for m in range(len(nums[i][j+1:])):
                    if nums[i][j+1+m] == 2:
                        k=j+1+m
                        break
                if 1 not in nums[i][j+1:k]:
                    cnt += 1


    print(f'#{tc+1} {cnt}')
