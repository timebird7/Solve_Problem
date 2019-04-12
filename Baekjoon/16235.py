import sys
from collections import deque

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

class Tree:
    def __init__(self,x,y,age):
        self.x = x
        self.y = y
        self.age = age

    def __repr__(self):
        return f'{self.x} {self.y} {self.age}'

N,M,K = map(int,sys.stdin.readline().split())
land = [[5 for i in range(N)] for j in range(N)]
A = [0]*N
trees = []
for n in range(N):
    A[n] = list(map(int,sys.stdin.readline().split()))
for n in range(M):
    tmp = list(map(int,sys.stdin.readline().split()))
    trees.append(Tree(tmp[0]-1,tmp[1]-1,tmp[2]))

trees.sort(key=lambda x: x.age)
trees = deque(trees)
for k in range(K):    
    die = []
    for i in range(len(trees)):
        if land[trees[i].x][trees[i].y] >= trees[i].age:
            land[trees[i].x][trees[i].y] -= trees[i].age
            trees[i].age += 1
        else:
            die.append(i) 

    die.sort(reverse=True)

    for d in die:
        land[trees[d].x][trees[d].y] += trees[d].age//2
        trees[:d+1].pop()

    for i in range(len(trees)):
        if trees[i].age%5 == 0:
            for j in range(8):
                nx = trees[i].x + dx[j]
                ny = trees[i].y + dy[j]
                if 0<=nx<=N-1 and 0<=ny<=N-1:
                    trees.appendleft(Tree(nx,ny,1))

    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]

    if not trees:
        break

print(len(trees))

     



