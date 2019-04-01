TC = int(input())

for tc in range(1,TC+1):
    V, E = map(int, input().split())
    edges = []

    for e in range(E):
        edges.append(list(map(int,input().split())))

    nums = [0 for i in range(V+1)]

    for edge in edges:
        if nums[edge[1]] == 0 or nums[edge[1]] > edge[2]:
            nums[edge[1]] = edge[2]

    print(f'#{tc} {sum(nums[1:])}')
