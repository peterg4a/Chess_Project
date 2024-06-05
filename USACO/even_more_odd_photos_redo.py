n = int(input())
line = input()
line = line.split()
cows = [int(i) for i in line]
even = 0
for i in cows:
    if i % 2 == 0:
        even += 1
odd = n - even
for i in range(50):
    if even > odd:
        print(2*odd + 1)
        break
    if even == odd:
        print(2*even)
        break
    else:
        even += 1
        odd -= 2