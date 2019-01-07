# N개의 숫자가 공백 없이 쓰여있다. 
# 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 5
# 54321
# 출력
# 15

n = int(input())
num1 = input()
result = 0

for x in range(0,n):
    result += int(num1[x])
print(result)
