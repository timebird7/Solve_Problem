
s = list(input())
t = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
result = 0
for x in range(0,len(s)):
    result += t[ord(s[x])-65]+1

print(result)