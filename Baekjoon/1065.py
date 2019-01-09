# 어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 110
# 출력
# 99
import sys

n = int(sys.stdin.readline())


if n < 100:
    print(n)
else:
    hs = []
    for x in range(1, 10):
        hs.append(x)

    for x in range(10, n+1):
        num = list(map(int, list(str(x))))
        m = len(num)
        dif = []
        for y in range(1, m):
            dif.append(num[y] - num[y-1])

        if dif.count(dif[0]) == len(dif):
            hs.append(x)

    print(len(hs))
