import sys

n = int(sys.stdin.readline())


strlist = [sys.stdin.readline().rstrip('\n') for x in range(0,n)]
strlist = list(set(strlist))
strlist.sort()
strlist.sort(key=len)



for x in strlist:
    print(x)