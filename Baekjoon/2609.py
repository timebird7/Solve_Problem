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

def gcd(a, b):
    if a == 1 or b == 1 :
        return 1
    elif a == b:
        return a
    elif is_prime(a) or is_prime(b):
        return 1
    else:
        for i in range(1, a+1):
            if a%i == 0 and b%i == 0:
                result = i
        return result

TC = 1

for i in range(TC):
    a, b = sorted(map(int,list(input().split())))
    print(gcd(a, b))
    print(lcm(a, b))                
