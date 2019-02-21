def game(x, y):
    if nums[x] == nums[y]:
        return x
    elif nums[x] == 2 and nums[y] == 1:
        return x
    elif nums[x] == 3 and nums[y] == 2:
        return x
    elif nums[x] == 1 and nums[y] == 3:
        return x
    elif nums[x] == 1 and nums[y] == 2:
        return y
    elif nums[x] == 2 and nums[y] == 3:
        return y
    elif nums[x] == 3 and nums[y] == 1:
        return y

def div(n, m):
    if n == m:
        return n
    elif n == m - 1:
        return game(n, m)
    else:
        pivot = (n+m)//2
        x = div(n, pivot)
        y = div(pivot+1, m)
        return game(x, y)

TC = int(input())

for tc in range(TC):
    n = int(input())
    nums = list(map(int, input().split()))
    
    ans = div(0, n-1)
    print(f'#{tc+1} {ans+1}')