import sys

nums =[]

for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip('\n')
    if s[0:2] == 'pu':
        nums.append(int(list(s.split())[-1]))
    elif s[0:2] == 'po':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
            nums.pop(0)
    elif s[0] == 's':
        print(len(nums))
    elif s[0] == 'e':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'f':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
    elif s[0] == 'b':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])

