def my_int(s):
    cnt = 0
    result = 0
    for i in s[::-1]:
        result += (ord(i)-48)*(10**cnt)
        cnt += 1
    return result

TC = int(input())
strlist = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for i in range(TC):
    T = input().split()
    wrdnum = my_int(T[1])
    s = input()
    slen = wrdnum*3 + (wrdnum + 1)

    cnt = [0 for x in range(10)]

    for j in range(slen-1):
        if j % 4 == 0:
            if s[j] == 'Z':
                cnt[0] += 1
            elif s[j] == 'O':
                cnt[1] += 1
            elif s[j+1] == 'W':
                cnt[2] += 1
            elif s[j+1] == 'H':
                cnt[3] += 1
            elif s[j+1] == 'O':
                cnt[4] += 1
            elif s[j+2] == 'V':
                cnt[5] += 1
            elif s[j+2] == 'X':
                cnt[6] += 1
            elif s[j+1] == 'V':
                cnt[7] += 1
            elif s[j] == 'E':
                cnt[8] += 1
            elif s[j] == 'N':
                cnt[9] += 1
    
    print(f'#{i+1}')

    for x in range(10):
        print(f'{strlist[x]} '*cnt[x],end='')