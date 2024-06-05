n = int(input())
times = []
for i in range(n):
    line = input().split()
    line = [int(i) for i in line]
    for i in range(line[0]):
        times.append(line[1])

times = sorted(times)

max_time = 0
for num in range(int(len(times)/2)):
    time = times[num]+times[(num*-1)-1]
    if time > max_time:
        max_time = time
print(max_time)