

s = input()


while s.find('c=') >= 0:
    s = s.replace('c=','1')
while s.find('c-') >= 0:
    s = s.replace('c-','2')
while s.find('dz=') >= 0:
    s = s.replace('dz=','3')
while s.find('d-') >= 0:
    s = s.replace('d-','4')
while s.find('lj') >= 0:
    s = s.replace('lj','5')
while s.find('nj') >= 0:
    s = s.replace('nj','6')
while s.find('s=') >= 0:
    s = s.replace('s=','7')
while s.find('z=') >= 0:
    s = s.replace('z=','8')

print(len(s))
