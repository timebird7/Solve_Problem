def my_len(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

TC = int(input())

for tc in range(TC):
    str1 = input()
    str2 = input()

    N = my_len(str1)
    M = my_len(str2)
    result = 0

    for i in range(M-N+1):
        
        if str2[i] == str1[0]:
            
            for j in range(1,N):
                if str2[i+j] != str1[j]:
                    break
            else:
                result = 1

    print(f'#{tc+1} {result}')

