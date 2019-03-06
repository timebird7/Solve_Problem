TC = int(input())

for tc in range(TC):
    a = list(map(int,input().split()))[1:]
    b = list(map(int,input().split()))[1:]
    ans = ''
    if a.count(4) > b.count(4):
        ans = 'A'
    elif a.count(4) == b.count(4) and a.count(3) > b.count(3):
        ans = 'A'
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) > b.count(2):
        ans = 'A'
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) == b.count(2) and a.count(1) > b.count(1):
        ans = 'A'

    if a.count(4) < b.count(4):
        ans = 'B'
    elif a.count(4) == b.count(4) and a.count(3) < b.count(3):
        ans = 'B'
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) < b.count(2):
        ans = 'B'
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) == b.count(2) and a.count(1) < b.count(1):
        ans = 'B'

    if not ans:
        ans = 'D'

    print(ans)