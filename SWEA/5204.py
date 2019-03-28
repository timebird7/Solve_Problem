def ms(nums):
    global cnt
    if len(nums) > 1:
        m = len(nums)//2
        left = ms(nums[:m])
        right = ms(nums[m:])

        if left[-1] > right[-1]:
            cnt += 1

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1

        if i < len(left):
            nums[k:k+len(left)] = left[i:]
            k += len(left)

        if j < len(right):
            nums[k:k+len(right)] = right[j:]
            k += len(right)

    return nums



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nums = list(map(int,input().split()))
    cnt = 0

    nums = ms(nums)

    print(f'#{tc} {nums[N//2]} {cnt}')
