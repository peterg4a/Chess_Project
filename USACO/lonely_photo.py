# n = int(input())
# cows = input()
# ans = 0
# for i in range(3, n+1, 1):
#     for j in range(n-i+1):
#         print(i,j)
#         group = []
#         for a in range(i):
#             group.append(cows[j+a])
#         g = 0
#         h = 0
#         for a in group:
#             if a == 'G':
#                 g += 1
#             else:
#                 h += 1
#         if g == 1 or h == 1:
#             ans += 1
# print(ans)

n = int(input())
cows = input()
ans = 0
for i in range(3, n+1, 1):
    g = 0
    h = 0
    for j in range(i):
        if cows[j] == 'G':
            g += 1
        else:
            h += 1
    if g == 1 or h == 1:
        ans += 1
    # print(g,h)
    for j in range(n-i):
        if cows[j] == 'G':
            g -= 1
        else:
            h -= 1
        if cows[j + i] == 'G':
            g += 1
        else:
            h += 1

        if g == 1 or h == 1:
            ans += 1
        # print(g,h)
print(ans)