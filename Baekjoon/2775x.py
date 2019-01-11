k = int(input())
f = []
f[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
f[1] = []
for t in range(k,0,-1):
    r += f[0][t]
    f[1][t] = r



print(f[1])