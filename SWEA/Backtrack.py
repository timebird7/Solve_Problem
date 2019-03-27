def backtrack(a, k, sum):
    if k == N:
        if sum == 10:
            tmp = []
            for i in range(1, 11):
                if a[i] == True:
                    tmp.append(i)
            print(tmp)
    else:
        k += 1
        if sum + k <= 10 :
            a[k] = 1
            backtrack(a, k, sum + k)
        a[k] = 0
        backtrack(a, k, sum)

N = 10
a = [0] * (N + 1)

backtrack(a, 0, 0)