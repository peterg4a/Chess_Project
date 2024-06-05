n = int(input())
peaks = []
for i in range(n):
    line = input()
    line = line.split()
    peaks.append([int(line[0]), int(line[1])])
peaks.sort()
visible = []
for current in peaks:
    if len(visible) == 0:
        visible.append(current)
    else:
        previous = visible[-1]

        #slope < 0
        if previous[1] > current[1]:
            #slope > -1
            if previous[1] - current[1] < current[0] - previous[0]:
                visible.append(current)
            #slope <= -1
            #do nothing

        #slope > 0
        elif previous[1] < current[1]:
            #slope < 1
            if current[0] - previous[0] > current[1] - previous[1]:
                visible.append(current)
            #slope >= 1
            else:
                for i in range(len(visible)-1, -1, -1):
                    x = visible[i]
                    if current[1] - x[1] < current[0] - x[0]:
                        break
                    else:
                        visible.pop(i)
                visible.append(current)
                        

        #slope = 0
        elif previous[1] == current[1]:
            visible.append(current)
print(len(visible))