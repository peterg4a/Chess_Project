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
    Max = min(hunger)
    Min = 0
    print(Max, Min)
    while True:
        hunger2 = [int(a) for a in line]
        mid = (Max+Min)//2
        print(mid)
        if Min == Max:
            x = calc(Max,hunger2)
            if x == None:
                print(-1)
                break
            else:
                print(x)
                break
        if calc(mid, hunger2) == None:
            Min = mid + 1
        else:
            Max = mid

    