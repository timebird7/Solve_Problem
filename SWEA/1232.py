def postord(root):
    global tree
    if tree[root][2]:
        if tree[root][2] == '+':
            a = postord(tree[root][0])
            b = postord(tree[root][1])
            return a+b
        elif tree[root][2] == '-':
            a = postord(tree[root][0])
            b = postord(tree[root][1])
            return a-b
        elif tree[root][2] == '*':
            a = postord(tree[root][0])
            b = postord(tree[root][1])
            return a*b
        elif tree[root][2] == '/':
            a = postord(tree[root][0])
            b = postord(tree[root][1])
            return a/b
        else:
            return int(tree[root][2])



for tc in range(1):
    N = int(input())

    tree = [[0, 0, 0] for i in range(N+1)]

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

    ans = postord(1)

    print('#{} {}'.format(tc+1, ans))