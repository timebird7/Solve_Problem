import copy
T = int(input())
ball = [1, 0, 0]

for i in range(T): 
    ball_ = copy.deepcopy(ball)   
    a, b = list(map(int,list(input().split())))
    
    ball_[a-1] = ball[b-1]
    ball_[b-1] = ball[a-1]

    ball = copy.deepcopy(ball_)

if sum(ball):
    print(ball.index(1)+1)
else:
    print(-1)

