stars = '''  *  
 * * 
*****'''

def star(n):
    if n == 3:
        return stars
    else:
        print(star(n/2))
        print(star(n/2)+star(n/2))


star(12)