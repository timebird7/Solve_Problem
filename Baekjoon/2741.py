# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())
nums = list(range(n,0,-1))
for x in nums:
    print(int(x))