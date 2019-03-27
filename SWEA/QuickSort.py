def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    for j in range(p,r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1

def qs(nums, l, r):
    if l < r:
        pivot = partition(nums, l, r)
        qs(nums, l, pivot-1)
        qs(nums, pivot+1, r)

nums = [11,45,22,81,23,34,99,22,17,8]

l = 0
r = len(nums) - 1
qs(nums,l,r)

print(nums)