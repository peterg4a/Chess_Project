n = int(input())
line = input()
line = line.split()
scores = [int(i) for i in line]

mins = []
for i in range(n):
    mins.append(10001)
x = 10001
for i in range(n-1, -1, -1):
    if scores[i] < x:
        x = scores[i]
    mins[i] = x

for i in range(n-2, -1, -1):
    scores[i] += scores[i + 1]

print(scores)
print(mins)

best_av = -1
K = []
for i in range(1, n-1):
    k = i
    least = mins[k]
    average = (scores[k] - least) / (n - k - 1)
    if average > best_av:
        best_av = average
        K = [k]
    elif average == best_av:
        K.append(k)
print(K)
