def calc(j, hunger2):
    food = 0
    for i in range(n-1):
        if hunger2[i] < j:
            return None
            break
        x = hunger2[i] - j
        hunger2[i] -= x
        hunger2[i+1] -= x
        food += 2*x
    if hunger2[n-1] == j:
        return food
    else:
        return None


T = int(input())
for i in range(T):
    n = int(input())
    line = input()
    line = line.split()
    hunger = [int(j) for j in line]
    x = min(hunger)
    for j in range(x, -2, -1):
        hunger2 = [int(a) for a in line]
        if j == -1:
            print(-1)
            break
        x = calc(j, hunger2)
        if x != None:
            print(x)
            break