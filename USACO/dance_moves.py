N, K = map(int, input().split())
swaps = [0 for i in range(K)]
for i in range(K):
    swaps[i] = list(map(int, input().split()))
cows = [i for i in range(N+1)]
start = [i for i in range(N+1)]
k = 0
counter = 2
z = True

while k != 0 and [i for i in cows] != [i for i in start] and z == False:
    z == False
    a, b = cows[k[0]], cows[k[1]]
    cows[k[0]] = b
    cows[k[1]] = a
    if k == K:
        k = 0
    else:
        k += 1

