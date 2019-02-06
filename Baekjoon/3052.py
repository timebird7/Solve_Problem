result = set()

for tc in range(10):
    num = int(input())
    temp = num%42

    result.add(num%42)

print(len(result))