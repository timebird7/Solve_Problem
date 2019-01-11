n = int(input())


ans = [1]

if n == 2:
    print(2)
else:

    for x in range(2,n):
        for t in range(0, 6*(x-1)):
            ans.append(x)
            if len(ans) > n-1:
                break
        else:
            continue
        break


    print(ans[-1])
