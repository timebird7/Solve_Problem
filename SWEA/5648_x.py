
TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    result = 0
    dots = []
    for n in range(N):
        dot = list(map(int,input().split()))
        dot[0] *= 2
        dot[1] *= 2
        dots.append([dot[0],dot[1],dot[2],dot[3]])

    for i in range(N):
        for j in range(i+1,N):
            if dots[i][0] == dots[j][0] and dots[i][1] > dots[j][1] and dots[i][2] == 1 and dots[j][2] == 0:
                result += dots[i][3]
            # elif dots[i][0] == dots[j][0] and dots[i][1] < dots[j][1] and dots[i][2] == 0 and dots[j][2] == 1:
            #     result += dots[i][3]
            elif dots[i][1] == dots[j][1] and dots[i][0] < dots[j][0] and dots[i][2] == 3 and dots[j][2] == 2:
                result += dots[i][3] 
            # elif dots[i][1] == dots[j][1] and dots[i][0] > dots[j][0] and dots[i][2] == 2 and dots[j][2] == 3:
            #     result += dots[i][3] 
            elif dots[j][0]-dots[i][0] == dots[j][1]-dots[i][1] and dots[i][2] == 3 and dots[j][2] == 1:
                result += dots[i][3]
            elif dots[j][0]-dots[i][0] == dots[i][1]-dots[j][1] and dots[i][2] == 1 and dots[j][2] == 2:
                result += dots[i][3]
            elif dots[j][0]-dots[i][0] == dots[i][1]-dots[j][1] and dots[i][2] == 3 and dots[j][2] == 0:
                result += dots[i][3]
            elif dots[j][0]-dots[i][0] == dots[j][1]-dots[i][1] and dots[i][2] == 0 and dots[j][2] == 2:
                result += dots[i][3]

    print(f'#{tc} {result}')