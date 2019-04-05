from copy import copy

def test(film):
    global D,W,K
    for j in range(W):
        flag = 0
        tmp = film[0][j]
        for i in range(1,D):            
            if tmp[-1] == film[i][j]:
                # tmp += film[i][j]
                tmp = '%s%s'%(tmp,film[i][j])
            else:
                tmp = film[i][j]

            if len(tmp) >= K:
                flag = 1
                break

        if flag == 0:
            return False
    return True

TC = int(input())

for tc in range(1,TC+1):
    D, W, K = map(int,input().split())
    nums = [0] * D

    for d in range(D):
        nums[d] = ''.join(input().split())

    # print(test(nums))

    queue = [(nums,[])]
    flag = 0
    ans = 0

    doping_a = '0'*W
    doping_b = '1'*W
    

    while True:
        tmp = []
        for q in queue:
            if test(q[0]) or K == 1:
                ans = len(q[1])
                flag = 1
                break
            for i in range(D):
                if i not in q[1]:                    
                    visited = copy(q[1])
                    visited.append(i)
                    film = copy(q[0])
                    film[i] = copy(doping_a)
                    if test(film):
                        ans = len(visited)
                        flag = 1
                        break
                    tmp.append((film,visited))
                    film = copy(q[0])
                    film[i] = copy(doping_b)
                    if test(film):
                        ans = len(visited)
                        flag = 1
                        break
                    tmp.append((film,visited))

            if flag:
                break
        if flag:
            print(f'#{tc} {ans}')
            break


        queue = copy(tmp)



        

