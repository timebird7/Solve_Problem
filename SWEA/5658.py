TC = int(input())

for tc in range(1,TC+1):
    N,K = map(int,input().split())
    num = input()
    nums = set()
    n = N//4
    for i in range(n):
        nums.add(num[:n])
        nums.add(num[n:2*n])
        nums.add(num[2*n:3*n])
        nums.add(num[3*n:])
        num = num[-1] + num[:-1]

    nnum = []

    for n in nums:
        nnum.append(int(n,16))

    nnum.sort(reverse=True)

    print(f'#{tc} {nnum[K-1]}')
