N = int(input())
tmp = [0] + list(map(int,input().split()))
line = []

for n in range(1,N+1):
    try:
        line = line[:len(line)-tmp[n]] + [n] + line[len(line)-tmp[n]:]
    except IndexError:
        line = [n] + line

for l in line:
    print(l,end=' ')