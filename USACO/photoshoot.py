
f = open('photo.in')
n = int(f.readline())
b = f.readline()
f.close()
b = b.split()
b = [int(i) for i in b ]
for number in range(b[0]):
    valid = True
    number = number + 1
    a = [number]
    used_numbers = []
    for i in range(n-1):
        if b[i] - a[i] in used_numbers or b[i] - a[i] < 1 or b[i] - a[i] > n:
            valid = False
            break
        if b[i] - a[i] not in used_numbers:
            used_numbers.append(b[i] - a[i])
        a.append(b[i] - a[i])
    
    if valid == True:
        break
answer = ''
answer = answer + str(a[0])
for i in range(n - 1):
    answer = answer + ' ' + str(a[i + 1])

f = open('photo.out', 'w')
f.write(answer)
f.close()