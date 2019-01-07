# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 10 5
# 1 10 4 9 2 3 8 5 7 6
# 출력
# 1 4 2 3

nnx = list(map(int, input().split()))
x = nnx[1]
nums = list(map(int, input().split()))
results = []
for y in nums:
    if y < x:
        results.append(y)
count = 0
for z in results:
    count += 1
    print(z, end='')
    if len(results) != count:
        print(' ', end='')
        
