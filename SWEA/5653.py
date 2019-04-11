class Cell:
    def __init__(self,x,y,e,de,flag):
        self.x = x
        self.y = y
        self.e = e
        self.de = de
        self.flag = flag

    def __repr__(self):
        return f'{self.x} {self.y} {self.e} {self.de} {self.flag}'

TC = int(input())

for tc in range(1,TC+1):
    N,M,K = map(int,input().split())

    nums = [0]*N
    for n in range(N):
        nums[n] = list(map(int,input().split()))

    cells = []
    history = {}

    for n in range(N):
        for m in range(M):
            if nums[n][m]:
                cells.append(Cell(n,m,nums[n][m],nums[n][m],0))
                history[(n,m)] = 1

    for k in range(K):
        cells.sort(key=lambda z: z.e, reverse=True)   
        tmp = []
        celltmp = []
        for i in range(len(cells)):
            if cells[i].flag == 1:
                if not history.get((cells[i].x-1,cells[i].y)):
                    celltmp.append(Cell(cells[i].x-1,cells[i].y,cells[i].e,cells[i].e,0))
                    history[(cells[i].x-1,cells[i].y)] = 1
                if not history.get((cells[i].x+1,cells[i].y)):
                    celltmp.append(Cell(cells[i].x+1,cells[i].y,cells[i].e,cells[i].e,0))
                    history[(cells[i].x+1,cells[i].y)] = 1
                if not history.get((cells[i].x,cells[i].y-1)):
                    celltmp.append(Cell(cells[i].x,cells[i].y-1,cells[i].e,cells[i].e,0))
                    history[(cells[i].x,cells[i].y-1)] = 1
                if not history.get((cells[i].x,cells[i].y+1)):
                    celltmp.append(Cell(cells[i].x,cells[i].y+1,cells[i].e,cells[i].e,0))
                    history[(cells[i].x,cells[i].y+1)] = 1

            if cells[i].flag == cells[i].e:
                tmp.append(i)
            else:
                cells[i].de -= 1
                if cells[i].de <= 0:
                    cells[i].flag += 1

        tmp.sort(reverse=True)

        for t in tmp:
            cells.pop(t)        
        cells.extend(celltmp)
        if not cells:
            break

    print(f'#{tc} {len(cells)}')


