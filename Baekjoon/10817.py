# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

# 입력
# 20 30 10
# 출력
# 20

nums = list(map(int, input().split()))
nums.sort()
print(nums[1])