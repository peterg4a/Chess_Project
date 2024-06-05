n = int(input())
Elsie = []
Bessie = []
points = 0

for i in range(n):
    Elsie.append(int(input()))
Elsie.sort()
print(Elsie)
x = 0
for i in range(2*n):
    num = i + 1
    if num != Elsie[x]:
        Bessie.append(num)
        print(num)
    else:
        x += 1
    if x > n:
        break
        
Elsie.sort(reverse = True)
Bessie.sort(reverse = True)

E_position = 0
B_position = 0
while E_position < n and B_position < n:
    E_card = Elsie[E_position]
    B_card = Bessie[B_position]
    if E_card > B_card:
        E_position += 1
    if B_card > E_card:
        B_position += 1
        E_position += 1
        points += 1

print(points)