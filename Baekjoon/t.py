
from time import time
def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    elif (n==3):
        return True
    elif (n==5):
        return True
    elif (n==7):
        return True
    elif (n==11):
        return True
    elif (n==13):
        return True
    elif (n==17):
        return True
    elif (n==19):
        return True
    elif (n==23):
        return True
    elif (n==29):
        return True
    elif (n==31):
        return True
    elif (n==37):
        return True
    elif (n==41):
        return True
    elif (n==43):
        return True
    elif (n==47):
        return True
    elif (n==53):
        return True
    elif (n==59):
        return True
    elif (n==61):
        return True
    elif (n==67):
        return True
    elif (n==71):
        return True
    elif (n==73):
        return True
    elif (n==79):
        return True
    elif (n==83):
        return True
    elif (n==89):
        return True
    elif (n==97):
        return True
    else:
        for x in range(2,int(n**0.5)+1):
            if(n % x==0):
                return False
        return True

s = time()

pnums = []
for i in range(5,1000000):
    if is_prime(i):
        pnums.append(i)

print(pnums)

print(time()-s)
