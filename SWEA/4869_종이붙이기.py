# def paper(N):
#     if N == 10:
#         return 1
#     elif N == 20:
#         return 3
#     else :
#         return paper(N-10) + paper(N-20)*2

def paper(N):
    global memo
    if N >= 30 and len(memo) <= N//10 - 1:
        memo.append(paper(N-10) + paper(N-20)*2)
    return memo[N//10 - 1]

memo = [1, 3]

TC = int(input())

for tc in range(TC):
    N = int(input())
    print(f'#{tc+1} {paper(N)}')

