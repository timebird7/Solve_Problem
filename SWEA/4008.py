# from itertools import permutations
# import time
# s = time.time()
# TC = int(input())

# for tc in range(1,TC+1):
#     N = int(input())
#     sign = list(map(int, input().split()))
#     nums = list(map(int, input().split()))

#     signs = '+'*sign[0] + '-'*sign[1] + '*'*sign[2] + '/'*sign[3]
#     ttt = set(permutations(signs))
#     results = set()
#     maxans = 0
#     minans = 10000000

#     for tt in ttt:
#         result = nums[0]
        
#         for i in range(len(tt)):
#             if tt[i] == '+':
#                 result += nums[i+1]
#             elif tt[i] == '-':
#                 result -= nums[i+1]
#             elif tt[i] == '*':
#                 result *= nums[i+1]
#             elif tt[i] == '/':
#                 result = int(result/nums[i+1])
#         maxans = max(result, maxans)
#         minans = min(result, minans)

#     print(f'#{tc} {maxans-minans}')
# print(time.time()-s)

def dfs(i, res):
    global n, mini, maxi, oper, num
    if i == n:
        if mini > res:
            mini = res
        if maxi < res:
            maxi = res
    if oper[0]:
        oper[0] -= 1
        dfs(i + 1, res + num[i])
        oper[0] += 1
    if oper[1]:
        oper[1] -= 1
        dfs(i + 1, res - num[i])
        oper[1] += 1
    if oper[2]:
        oper[2] -= 1
        dfs(i + 1, res * num[i])
        oper[2] += 1
    if oper[3]:
        oper[3] -= 1
        dfs(i + 1, int(res / num[i]))
        oper[3] += 1


for TC in range(1, int(input()) + 1):
    n = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    mini = 100000000
    maxi = -100000000
    dfs(1, num[0])
    print("#{} {}".format(TC, maxi - mini))