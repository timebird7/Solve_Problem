# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 5
# 출력
# *
# **
# ***
# ****
# *****

n = int(input())
nums = list(range(1,n+1))
for x in nums:
    print('*'*x)