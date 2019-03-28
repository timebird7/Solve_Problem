TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    cnt = 0
    A = sorted(map(int, input().split()))
    B = map(int, input().split())  

    for b in B:
        if b not in A:
            continue
        l = 0
        r = N - 1
        m = (l+r)//2
        tmp = '0'        
        while True:            
            if b >= A[l] and b <= A[m-1]:
                if tmp == 'l':
                    break
                tmp = 'l'
                r = m - 1
                m = (l+r)//2
            if b >= A[m+1] and b <= A[r]:
                if tmp == 'r':
                    break
                tmp = 'r'
                l = m + 1
                m = (l+r)//2
            if b == A[m]:
                cnt += 1
                break

    print(f'#{tc} {cnt}')


