n = int(input())
a = input()
a = a.split()
a = [int(i) for i in a]
a.sort()
b = input()
b = b.split()
b = [int(i) for i in b]
b.sort()
ans = 1
x = 0
for i in range(n-1, -1, -1):
    num = 0
    for j in range(n):
        if a[i] <= b[j]:
            num = num + 1
    
    ans = ans * (num - x)
    x = x + 1
print(ans)