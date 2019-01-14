n = list(input())

n.sort(key=int)
n.reverse()

for x in n:
    print(x, end='')