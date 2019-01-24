T = input()

n = int(T)
l = len(T)

for i in range(n-9*l,n+1):
    nums = list(map(int, list(str(i))))

    if sum(nums) + i == n:
        print(i)
        break

else:
    print(0)