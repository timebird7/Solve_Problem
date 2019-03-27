T = input()

n = int(T)
l = len(T)
ans = [0,0,1,0,2,0,3,0,4,0,5,10,6,11,7,12,8,13]

if int(T) <= 17:
    print(ans[int(T)])
else:
    for i in range(n-9*l,n+1):
        nums = list(map(int, list(str(i))))

        if sum(nums) + i == n:
            print(i)
            break

    else:
        print(0)