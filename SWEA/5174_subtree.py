def preord(root):
    global tree
    global flag
    global cnt
    global N
    if root == N:
        flag = 1
    if root and flag:
        cnt += 1
        preord(tree[root][0])
        preord(tree[root][1])
        if root == N:
            flag = 0
    elif root:
        preord(tree[root][0])
        preord(tree[root][1])


TC = int(input())

for tc in range(TC):
    E, N = list(map(int,input().split()))
    ways = list(map(int,input().split()))

    tree = [[0,0,0] for i in range(max(ways)+1)]

    for e in range(E):
        if tree[ways[2*e]][0] == 0:
            tree[ways[2*e]][0] = ways[2*e+1]
            tree[ways[2*e+1]][2] = ways[2*e]
        else:
            tree[ways[2*e]][1] = ways[2*e+1]
            tree[ways[2 * e+1]][2] = ways[2 * e]

    for i in range(1,max(ways)+1):
        if tree[i][2] == 0:
            root = i
            break

    flag = 0
    cnt = 0

    preord(root)

    print('#{} {}'.format(tc + 1, cnt))