TC = int(input())

for tc in range(TC):
    N = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    visited = [0] * (sum(scores) + 1)
    
    for n in range(N):        
        tmp = [scores[n]]
        for m in range(len(visited)):
            if visited[m]:                
                tmp.append(m+scores[n])
        else:
            for t in tmp:
                visited[t] = 1

    visited[0] = 1
    print("#{} {}".format(tc+1, sum(visited)))