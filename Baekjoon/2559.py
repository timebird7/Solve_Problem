N, K = list(map(int,input().split()))
temp = list(map(int,input().split()))
res = sum(temp[0:K])
s = sum(temp[0:K])
for i in range(1,N-K+1):
    s -= temp[i-1]
    s += temp[i+K-1]
    if s > res:
        res = s

print(res)