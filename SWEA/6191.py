from itertools import product

def test(n):
    if n.count('a') != n.count('b'):
        return False
    for i in range(len(n)):
        if n[i] == 'b':
            if n[:i+1].count('a') >= n[:i+1].count('b'):
                continue
            else:
                return False
    return True


TC = int(input())

for tc in range(1,TC+1):
    N,K = map(int,input().split())
    num = ['a','b']
    nums = product(num,repeat=2*N)
    tnums = []
    for n in nums:
        if test(n):
            tnums.append(n)


    tnums = sorted(list(map(lambda x:''.join(x), tnums)))

    try:
        tmp = tnums[K-1]
        tmp = tmp.replace('a','(')
        tmp = tmp.replace('b',')')
        print(f'#{tc} {tmp}')
    except IndexError:
        print(f'#{tc} )(')
