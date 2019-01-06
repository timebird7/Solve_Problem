# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# 입력
# 5
# 출력
# *****
# ****
# ***
# **
# *


n = int(input())

nums = list(range(n,0,-1))

for x in nums:
    
    print('*'*x)