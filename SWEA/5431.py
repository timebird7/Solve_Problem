TC = int(input())

for tc in range(TC):
    N, K = list(map(int,input().split()))
    nums1 = list(map(int,input().split()))
    nums2 = list(range(1,N+1))
    print(f'#{tc+1}',end='')

    for i in nums2:
        cnt = 0
        for j in nums1:
            if i == j:
                cnt += 1
            
        if cnt == 0 :
            print(f' {i}',end='')

    print()