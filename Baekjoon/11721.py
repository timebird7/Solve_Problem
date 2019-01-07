# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

# 입력
# BaekjoonOnlineJudge
# 출력
# BaekjoonOn
# lineJudge

sentence = input()
n = len(sentence)
m = n//10

for x in range(0,m+1):
    k = (x+1)*10
    print(sentence[x*10:k])

    