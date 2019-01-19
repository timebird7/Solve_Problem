n = int(input())


cnt = 1
result = 1

while cnt < n:
    cnt += result * 6
    result += 1

print(result)



# n = int(input())


# ans = [1]

# if n == 2:
#     print(2)
# else:

#     for x in range(2,n):
#         for t in range(0, 6*(x-1)):
#             ans.append(x)
#             if len(ans) > n-1:
#                 break
#         else:
#             continue
#         break

# print(ans)
# #     print(ans[-1])

# ans = '1'
# for x in range(2,int(n/4)):
#     ans += f'{x}'*6*(x-1)
#     if len(ans) > n:
#         print(x)
#         break


