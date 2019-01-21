TC = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
c = list(zip(b, a))

result = 0
for x,y in c:
    result += x*y

print(result)

