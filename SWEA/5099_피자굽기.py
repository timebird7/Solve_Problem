TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    pizza = [[i+1,nums[i]] for i in range(M)]
    queue = []

    for i in range(N):
        queue.append(pizza.pop(0))

    while True:
        tmp = queue.pop(0)
        if queue:
            tmp[1] //= 2

            if tmp[1]:
                queue.append(tmp)
            else:
                if pizza:
                    queue.append(pizza.pop(0))

        else:
            break

    print(f'#{tc+1} {tmp[0]}')



    