def perm_re(cnt):
    if cnt == 5:
        perms.append(perm[:5])
        return
    perm[cnt] = 0
    perm_re(cnt+1)
    perm[cnt] = 1
    perm_re(cnt+1)

perms = []
perm = [0] * 10
perm_re(0)

print(perms)