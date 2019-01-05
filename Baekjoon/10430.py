# (A+B)%C는 (A%C + B%C)%C 와 같을까?

# (A×B)%C는 (A%C × B%C)%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
# 5 8 4
# 출력
# 1
# 1
# 0
# 0

A, B, C = list(map(int, input().split()))
resa = (A+B)%C
resb = ((A%C) + (B%C))%C
resc = (A*B)%C
resd = ((A%C) * (B%C))%C
print(int(resa))
print(int(resb))
print(int(resc))
print(int(resd))