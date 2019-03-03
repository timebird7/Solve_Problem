import random
import time

data = [random.randint(1,100) for _ in range(20000)]

# data = [1, 5, 2, 4, 3, 9, 10, 8, 6, 7]

data1 = data[:]

st = time.time()

pQ = [101] * (len(data) + 10)
f = r = -1
r += 1; pQ[r] = data[0]

for i in range(1, len(data)):
    pos = r + 1
    for j in range(r, f, -1):
        if pQ[j] > data[i] :
            pQ[j+1] = pQ[j]
            pos -= 1

    pQ[pos] = data[i]
    r += 1

for _ in range(10):
    f += 1; print(pQ[f])

print(time.time() - st)






class Node :
    def __init__(self, item, n=None):
        self.item = item
        self.next = n


def enPQueue(item) :
    global front, rear
    newNode = Node(item)
    if front == None :
        front = newNode
    else :
        f = front
        pre = None
        while f :
            if f.item < newNode.item :
                pre = f
                f = f.next
            else:
                break
        if pre == None :
            front = newNode
            newNode.next = f
        elif f == None:
            pre.next = newNode
            rear= newNode
        else:
            pre.next = newNode
            newNode.next = f


def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None :
        front = newNode
    else :
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear
    if front == None:
        print("Queue_Empty")
        return None

    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

def printQ10() :
    f = front
    for i in range(10):
        print(f.item)
        f = f.next


st = time.time()

front = None
rear = None
for i in range(len(data)):
    enPQueue(data1[i])
    # enQueue(data[i])

printQ10()

print(time.time() - st)