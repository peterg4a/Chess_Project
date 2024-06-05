n, k = map(int, input().split())
cows = [int(input()) for i in range(n)]
cows.sort()
cows2 = [0 for i in range(n)]
for i in range(n):
    cows2[i] = cows[i]%12 + 1
gaps = [0 for i in range(n-1)]
for i in range(n-1):
    gaps[i] = cows[i+1] - cows[i] - 1
gaps.sort()
