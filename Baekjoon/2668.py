N = int(input())
nums = []
flag = 0

for i in range(1,N+1):
    nums.append([i,int(input())])

while True:
    tmp = set([num[1] for num in nums])
    lst = []

    for num in nums:
        if num[0] in tmp:
            lst.append(num)

    else:
        tmp1 = set([num[0] for num in lst])
        tmp2 = set([num[1] for num in lst])

        if tmp1 == tmp2:
            flag = 1

    if flag:
        break

    nums = lst

tmp = list(tmp)
tmp.sort()
print(len(tmp))
for t in tmp:
    print(t)


