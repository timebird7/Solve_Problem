N = int(input())
ropes = [0 for n in range(N)]
mw = 0

for n in range(N):
    ropes[n] = int(input())

ropes.sort(reverse=True)

for i in range(len(ropes)):
    if ropes[i]*(i+1) > mw:
        mw = ropes[i]*(i+1)

print(mw)


