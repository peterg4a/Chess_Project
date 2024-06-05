# n = int(input())
# row = input()
# patterns = []
# for k in range(n):
#     k = k + 1
#     go = 'no'
#     for i in range(n-k+1):
#         pattern = ''
#         for j in range(k):
#             pattern = pattern + row[i+j]
#         if pattern in patterns:
#             go = 'yes'
#             print(patterns)
#             patterns.clear()
#             break
#         else:
#             patterns.append(pattern)
#     if go == 'no':
#         print(k)
#         break


f = open('whereami.in')
n = int(f.readline())
row = f.readline()
f.close()
patterns = []
for k in range(n):
    k = k + 1
    go = 'no'
    for i in range(n-k+1):
        pattern = ''
        for j in range(k):
            pattern = pattern + row[i+j]
        if pattern in patterns:
            go = 'yes'
            print(patterns)
            patterns.clear()
            break
        else:
            patterns.append(pattern)
    if go == 'no':
        f = open('whereami.out', 'w')
        f.write(str(k))
        f.close()
        break
