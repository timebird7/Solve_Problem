class Atom:
    def __init__(self, x, y, d, e):
        self.x = x
        self.y = y
        self.d = d
        self.e = e

    def move(self):
        if self.d == 0:
            self.y += 1
        elif self.d == 1:
            self.y -= 1
        elif self.d == 2:
            self.x -= 1
        elif self.d == 3:
            self.x += 1
    
    def boom(self):
        global result
        result += self.e

    def check(self):
        if -2000<=self.x<=2000 and -2000<=self.y<=2000:
            return True
        else:
            return False

        
TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    result = 0
    atoms = [0]*N

    for n in range(N):
        o = list(map(int,input().split()))
        atoms[n] = Atom(o[0]*2,o[1]*2,o[2],o[3])

    for t in range(4001):
        tmp = []
        for i in range(len(atoms)):
            atoms[i].move()
            if not atoms[i].check():
                tmp.append(i)

        tmp = sorted(tmp,reverse=True)

        for i in tmp:
            atoms.pop(i)

        tmp = set()

        for i in range(len(atoms)):
            for j in range(i+1,len(atoms)):
                if atoms[i].x == atoms[j].x and atoms[i].y == atoms[j].y:
                    tmp.add(i)
                    tmp.add(j)

        tmp = sorted(tmp,reverse=True)

        for i in tmp:
            atoms[i].boom()
            atoms.pop(i)

        if not atoms:
            break

    print(f'#{tc} {result}')




