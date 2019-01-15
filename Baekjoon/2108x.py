#답나옴, 시간초과


import sys

n = int(sys.stdin.readline())
numlist = [int(sys.stdin.readline().rstrip('\n')) for x in range(0,n)]


print(round(sum(numlist)/n))

print(sorted(numlist)[n//2])



newlist = sorted(sorted(numlist), key=numlist.count, reverse=True)
m = newlist.count(newlist[0])
if n == 1:
    print(newlist[0])
elif newlist.count(newlist[m]) == m:
    print(newlist[m])
else:
    print(newlist[0])


print(max(numlist)-min(numlist))