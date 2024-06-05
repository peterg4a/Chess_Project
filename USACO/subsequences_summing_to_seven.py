# n = int(input())
# cows = []
# for i in range(n):
#     cows.append(int(input()))
# for i in range(n-1):
#     cows[i+1] += cows[i]
# print(cows)
# ans = 0
# x = False
# for i in range(n-1, -1, -1):
#     for j in range(n - i):
#         if j == 0:
#             num = cows[j+i]
#         else:
#             num = cows[j + i] - cows[j - 1]

#         if num % 7 == 0:
#             ans = i + 1
#             x = True
#             break
#     if x == True:
#         break
# print(ans)

n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))
for i in range(n):
    if i == 0:
        cows[i] = cows[i] % 7
    else:
        cows[i] = cows[i] % 7 + cows[i-1]
print(cows)
ans = 0
x = False
for i in range(n-1, -1, -1):
    print('length is ', i+1)
    for j in range(n):
        if j == 0:
            num = cows[j + i]
        else:
            num = cows[j + 1] - cows[j - 1]
        print(num)
        if num % 7 == 0:
            ans = i+1
            x = True
            break
    if x == True:
        break
print(ans)