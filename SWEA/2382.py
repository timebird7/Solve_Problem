nd = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


class Germ:
    def __init__(self, x, y, e, d):
        self.x = x
        self.y = y
        self.e = e
        self.d = d

    def move(self):
        if self.d == 1:
            self.x -= 1
        elif self.d == 2:
            self.x += 1
        elif self.d == 3:
            self.y -= 1
        elif self.d == 4:
            self.y += 1

    def check(self):
        global N
        if 0<self.x<N-1 and 0<self.y<N-1:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.x},{self.y},{self.e},{self.d}'

    def __repr__(self):
        return f'{self.x},{self.y},{self.e},{self.d}'

TC = int(input())

for tc in range(1,TC+1):
    N,M,K = map(int,input().split())
    result = 0
    germs = [0]*K

    for k in range(K):
        o = list(map(int,input().split()))
        germs[k] = Germ(o[0],o[1],o[2],o[3])

    for m in range(M):
        
        tmp = []
        for i in range(len(germs)):
            germs[i].move()
            if not germs[i].check():
                germs[i].d = nd[germs[i].d]
                germs[i].e //= 2
                if germs[i].e == 0:
                    tmp.append(i)

        tmp.sort(reverse=True)

        for t in tmp:
            germs.pop(t)

        tmp = set()

        germs.sort(key=lambda x:x.e, reverse=True)

        for i in range(len(germs)):
            for j in range(i+1,len(germs)):
                if germs[i].x == germs[j].x and germs[i].y == germs[j].y:
                    germs[i].e += germs[j].e
                    tmp.add(j)

        tmp = sorted(tmp,reverse=True)
        
        for t in tmp:
            germs.pop(t)


    for germ in germs:
        result += germ.e

    

    print(f'#{tc} {result}')


