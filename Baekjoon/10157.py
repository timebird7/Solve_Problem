import sys

def cango(i,j):
    global seats
    if i<0 or i>N-1 or j<0 or j>N-1:
        return False
    if seats[i][j]:
        return False
    return True

C, R = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())

seats = [[0]*R for i in range(C)]

print(seats)