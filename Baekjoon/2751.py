n = int(input())
numlist = []
for x in range(0,n):
    numlist.append(input())

numlist.sort(key=int)

for x in numlist:
    print(x)