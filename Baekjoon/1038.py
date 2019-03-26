N = int(input())

if N >= 1023:
    print(-1)
else:
    nums = ['0','1','2','3','4','5','6','7','8','9']
    i = 0
    while True:
        tmp = nums[i]
        j = int(tmp[-1])
        for k in range(j):
            nums.append(tmp+str(k))

        if len(nums)-1 >= N:
            break

        i += 1

    print(nums[N]) 
