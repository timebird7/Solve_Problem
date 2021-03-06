def convert(pwd):
    result = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if pwd[7*i:7*i+7] == '0001101':
            result[i] = 0
            continue
        if pwd[7*i:7*i+7] == '0011001':
            result[i] = 1
            continue
        if pwd[7*i:7*i+7] == '0010011':
            result[i] = 2
            continue
        if pwd[7*i:7*i+7] == '0111101':
            result[i] = 3
            continue
        if pwd[7*i:7*i+7] == '0100011':
            result[i] = 4
            continue
        if pwd[7*i:7*i+7] == '0110001':
            result[i] = 5
            continue
        if pwd[7*i:7*i+7] == '0101111':
            result[i] = 6
            continue
        if pwd[7*i:7*i+7] == '0111011':
            result[i] = 7
            continue
        if pwd[7*i:7*i+7] == '0110111':
            result[i] = 8
            continue
        if pwd[7*i:7*i+7] == '0001011':
            result[i] = 9
            continue
    
    return result

TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = ['' for i in range(N)]
    pwd = ''

    for n in range(N):
        nums[n] = input()

    for n in range(n):
        if int(nums[n]):
            for i in range(M-1,-1,-1):
                if int(nums[n][i]):
                    pwd = nums[n][i-55:i+1]
                    break

        if pwd:
            break
    
    code = convert(pwd)

    result = (code[0] + code[2] + code[4] + code[6]) * 3 + (code[1] + code[3] + code[5]) + code[7]

    if result%10 == 0:
        print(f'#{tc+1} {sum(code)}')
    else:
        print(f'#{tc+1} 0')
