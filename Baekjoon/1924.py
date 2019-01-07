# 오늘은 2007년 1월 1일 월요일이다. 
# 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 입력
# 1 1
# 출력
# MON

# 입력
# 3 14
# 출력
# WED

date = input()
datelen = len(date)

for x in range(0,datelen):
    if date[x] == ' ':
        sepa = x

month = int(date[0:sepa])
day = int(date[(sepa+1):])

daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
daynum = 0
if month != 1:
    for y in range(0,month-1):
    
        daynum += daylist[y]
daynum += day

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(days[daynum%7])