x = []
for i in range(10000):
    x.append(i)
x.sort()
l = 0
r = len(x)
num = 9999
while True:
    print(1)
    mid = (r+l)//2
    if x[mid] == num:
        print(num)
        break
    elif x[mid] > num:
        r = mid
    else:
        l = mid