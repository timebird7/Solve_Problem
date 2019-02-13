M = 0   # 길이
s = ''  # 문자열

def isPalinH(x,y):
    for i in range(M//2):
        if s[x][y+i] != s[x][y+(M-1)-i]:
            return False
    return True

def isPalinV(x,y):
    for i in range(M//2):
        if s[x+i][y] != s[x+(M-1)-i][y]:
            return False
    return True