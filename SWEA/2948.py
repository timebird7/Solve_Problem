TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    
    a = set(input().split())
    b = set(input().split())
    
    c = a.intersection(b)
    print(f'#{tc} {len(c)}')