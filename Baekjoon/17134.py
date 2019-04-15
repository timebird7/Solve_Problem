import sys

t = 1000000
a = [1]*(t+1)
for i in range(2,int(t**.5)):
    a[i*2::i]=[0]*((t-i)//i)

for i in range(int(sys.stdin.readline())):

    n = int(sys.stdin.readline())
    cnt = 0


    for x in range(3,n):
        if  a[x] and a[(n-x)//2]:
            cnt += 1

    print(cnt)