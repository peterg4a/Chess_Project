import math
n = int(input())
id = input()
id = id.split()
id = [int(i) for i in id ]

even = 0
for i in range(n):
    if id[i] % 2 == 0:
        even = even + 1
odd = n - even
while True:
    if even == odd or even - 1 == odd:
        break
    else:
        if odd > even:
            even = even + 1 
            odd = odd - 2
        else:
            even = even - 1
print(even + odd)