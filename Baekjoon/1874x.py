# 답나옴, 시간초과

n = int(input())
nums = [0 for i in range(n)]

for i in range(n):
    nums[i] = int(input())

pnt = 0
stack = [0]
result = []
ans = []

while True:
    for i in range(1,n+1):
        if nums[pnt] == stack[-1]:
            result.append(stack.pop(-1))
            ans.append('-')
            pnt += 1
            break
        elif i not in stack and i not in result:
            stack.append(i)
            ans.append('+')

        elif nums[pnt] != stack[-1] and nums[pnt] in stack:
            ans.append('NO')
            break

    if len(result) == n:
        for a in ans:
            print(a)
        break

    if ans[-1] == 'NO':
        print('NO')
        break
    

   


