def inord(root):
    global tree
    global ans
    if root:
        inord(tree[root][0])
        ans += tree[root][2]
        inord(tree[root][1])


for tc in range(10):
    N = int(input())

    tree = [[0, 0, 0] for i in range(N+1)]
    ans = ''

    for n in range(N):
        s = input().split()
        tree[int(s[0])][2] = s[1]
        try:
            tree[int(s[0])][0] = int(s[2])
        except IndexError:
            continue
        try:
            tree[int(s[0])][1] = int(s[3])
        except IndexError:
            continue

    inord(1)

    print('#{} {}'.format(tc+1, ans))



