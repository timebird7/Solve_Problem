TC = int(input())

for i in range(TC):
    H, W = list(map(int,list(input().split())))
    result = []
    
    for j in range(H):
        result.append(input())

    for j in reversed(result):
        print(j)
