result = 0
score = 0

for tc in range(5):
    nums = list(map(int,input().split()))

    if sum(nums) > score :
        score = sum(nums)
        result = tc + 1

print(f'{result} {score}')
