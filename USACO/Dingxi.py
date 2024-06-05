# def calc(x, past):
#     if past[-1] == n:
#         paths.append(past)
#         return
#     for i in range(3):
#         end = x+1+i
#         if end <= n:
#             if stairs[end]:
#                 calc(x+end, past+[end])

# line = input()
# line = line.split()
# n, k = [int(i) for i in line]
# line = input()
# line = line.split()
# broken = [int(i) for i in line]
# stairs = []
# for i in range(n+1):
#     stairs.append(True)
# for i in broken:
#     stairs[i] = False
# paths = []
# calc(0, [0])
# print(paths)
# print(len(paths))



def calc(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(3):
        end = x+1+i
        if end <= n:
            if stairs[end]:
                calc(end)

line = input()
line = line.split()
n, k = [int(i) for i in line]
if k == 0:
    print(1)
else:
    line = input()
    line = line.split()
    broken = [int(i) for i in line]
    stairs = []
    for i in range(n+1):
        stairs.append(True)
    for i in broken:
        stairs[i] = False
    print(stairs)
    ans = 0
    calc(0)
    print(ans)