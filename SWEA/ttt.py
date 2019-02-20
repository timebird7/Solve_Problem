def backtrack(a, k, input):
    global MAXCANDIDATES
    global ans
    c = [0] * MAXCANDIDATES

    if k == input:
        r = []
        for i in range(1,11):
            if a[i] == True:
                r.append(i)
        ans.append(r)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 11
NMAX = 11
a = [0] * NMAX
ans = []
backtrack(a, 0, 10)

for i in ans:
    if sum(i) == 10:
        print(i)