n = int(input())
line = input()
line = line.split()
List = [int(i) for i in line]

f = [0]
for i in range(n):
    f.append(max(f[i]+List[i], List[i]))

print(max[f])