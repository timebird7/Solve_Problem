n = int(input())
numlist = []
for x in range(0,n):
    numlist.append(int(input()))

print(round(sum(numlist)/n))

print(sorted(numlist)[n//2])

# 최빈값 여러개있을때 두번째로 작은수 어떻게????
if n == 1:
    print(numlist[0])
else:
    m = max(sorted(numlist), key=numlist.count)
    cnt = numlist.count(m)
    


print(max(numlist)-min(numlist))