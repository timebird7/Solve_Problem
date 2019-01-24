def findpurple(paper):
    result = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                result += 1
    return result    

TC = int(input())

for i in range(TC):
    paper = [[0 for x in range(10)]for y in range(10)]

    T = int(input())

    for j in range(T):
        nums = list(map(int,list(input().split())))

        for a in range(nums[0],nums[2]+1):
            for b in range(nums[1],nums[3]+1):
                paper[a][b] += nums[4]

    print(f'#{i+1} {findpurple(paper)}')
