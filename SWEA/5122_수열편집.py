TC = int(input())

for tc in range(TC):
    N, M, L = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    for m in range(M):
        x = input().split()
        if x[0] == 'I':
            nums.insert(int(x[1]),int(x[2]))
        elif x[0] == 'D':
            nums.pop(int(x[1]))
        elif x[0] == 'C':
            nums[int(x[1])] = int(x[2])

    try:
        print(f'#{tc+1} {nums[L]}')
    except IndexError:
        print(f'#{tc+1} -1')    