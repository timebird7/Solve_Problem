def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,int(n**0.5)+1):
            if(n % x==0):
                return False
        return True

def lcm(a, b):
    if a == 1 or b == 1 :
        return a*b
    elif a == b:
        return a
    elif is_prime(a) and is_prime(b):
        return a*b
    else:
        n = a
        m = b
        while a != b :
            while a < b:
                a += n           
            while b < a:
                b += m            
            if a == b:
                return a

TC = int(input())

for i in range(TC):
    a, b = sorted(map(int,list(input().split())))
    print(lcm(a, b))