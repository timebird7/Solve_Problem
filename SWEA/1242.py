def makebi(M):
    M = M.replace('0','0000')
    M = M.replace('1','0001')
    M = M.replace('2','0010')
    M = M.replace('3','0011')
    M = M.replace('4','0100')
    M = M.replace('5','0101')
    M = M.replace('6','0110')
    M = M.replace('7','0111')
    M = M.replace('8','1000')
    M = M.replace('9','1001')
    M = M.replace('A','1010')
    M = M.replace('B','1011')
    M = M.replace('C','1100')
    M = M.replace('D','1101')
    M = M.replace('E','1110')
    M = M.replace('F','1111')
    return M
 
def divcode(binum, codes):
    binum = binum.lstrip('0')
    tmp = ''
    flag = '0'
    for b in binum:
        if b != flag[-1]:
            flag += b
             
        if len(flag) > 32:
            flag = '0'
            a = 56 - len(tmp)%56
            tmp = '0'*a + tmp
            codes.add(tmp)
            tmp = ''
        elif len(flag) > 1 and len(flag) <= 32:
            tmp += b
    return codes
 
def convert(pwd, x):
    result = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if pwd[7*x*i:7*x*i+7*x] == '000'*x + '11'*x + '0'*x + '1'*x:
            result[i] = 0
            continue
        if pwd[7*x*i:7*x*i+7*x] == '00'*x + '11'*x + '00'*x + '1'*x:
            result[i] = 1
            continue
        if pwd[7*x*i:7*x*i+7*x] == '00'*x + '1'*x + '00'*x + '11'*x:
            result[i] = 2
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1111'*x + '0'*x + '1'*x:
            result[i] = 3
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1'*x + '000'*x + '11'*x:
            result[i] = 4
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '11'*x + '000'*x + '1'*x:
            result[i] = 5
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '1'*x + '0'*x + '1111'*x:
            result[i] = 6
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '111'*x + '0'*x + '11'*x:
            result[i] = 7
            continue
        if pwd[7*x*i:7*x*i+7*x] == '0'*x + '11'*x + '0'*x + '111'*x:
            result[i] = 8
            continue
        if pwd[7*x*i:7*x*i+7*x] == '000'*x + '1'*x + '0'*x + '11'*x:
            result[i] = 9
            continue
 
    return result
 
TC = int(input())
 
for tc in range(1,TC+1):
    N, M = list(map(int,input().split()))
    nums = set()
    ans = 0
    codes = set()
 
    for n in range(N):
        tmp = input().lstrip('0')
        if tmp:
            nums.add(tmp)
     
    for n in nums:
        binum = makebi(n)
        codes = divcode(binum, codes)
 
    for code in codes:
        x = len(code)//56
        pwd = convert(code,x)
 
        result = (pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + (pwd[1] + pwd[3] + pwd[5]) + pwd[7]
 
        if result%10 == 0:
            ans += sum(pwd)
        else:
            continue
 
    print(f'#{tc} {ans}')