N = int(input())
P = list(map(int,input().split()))
result = 0
results = []

for i in range(1, N):
    if P[i] > P[i-1]:
        result += P[i] - P[i-1]

    else : 
        results.append(result)
        result = 0

else :
    results.append(result)

if results :
    print(max(results))
else:
    print(0)