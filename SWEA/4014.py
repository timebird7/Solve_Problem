from copy import deepcopy


def test(road,x):
    global N
    i = 0
    while True:
        if i+x<=N-1:
            if road[i+x] - 1 == road[i]:
                for k in road[i:i+x]:
                    if k != road[i]:
                        return False

                i = i+x-1


        elif road[i+1] + 1 == road[i]:
            if i+x<=N-1:
                for k in road[i+1:i+x+1]:
                    if k != road[i] - 1:
                        return False
            else:
                return False
            i = i+x-1

        i += 1

        if i >= len(road)-1:
            return True

TC = int(input())

for tc in range(1,TC+1):
    N,X = map(int,input().split())
    cnt = 0

    nums = [0]*N
    for n in range(N):
        nums[n] = list(map(int,input().split()))
        if test(nums[n],X):
            cnt += 1

    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(nums[i][j])

        if test(tmp,X):
            cnt += 1

    print(f'#{tc} {cnt}')
