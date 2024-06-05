import heapq
def check():
    time = 0
    next_cow = 0
    stage = []
    for i in range(mid):
        stage.append(0)
    
    while next_cow < n:
        shortest = heapq.heappop(stage)
        heapq.heappush(stage, shortest + cows[next_cow])
        next_cow += 1

    return(max(stage) < t)

line = input()
line = line.split()
n, t = int(line[0]), int(line[1])
cows = []
for i in range(n):
    cows.append(int(input()))

l, r = 1, n
while l+1 < r:
    mid = (l+r)//2

    if check():
        r = mid
    else:
        l = mid
print(mid)