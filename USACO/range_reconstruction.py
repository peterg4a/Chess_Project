def in_range(ans):
    for Range in List2:
        if max(ans[Range[0] : Range[1]+1]) - min(ans[Range[0] : Range[1]+1]) != Range[2]:
            #print('no good', ans, Range)
            return False
    return True

def recursion(index, ans):
    global x
    if not x:
        return
    #print(ans)
    if index == n+1:
        if in_range(ans):
            x = False
            global ans2
            ans2 = [i for i in ans]
            #print(ans2)
            return

    else:
        recursion(index+1, ans+[ans[index-1] + all_ranges[index-1][index]])

        recursion(index+1, ans+[ans[index-1] - all_ranges[index-1][index]])




n = int(input())
List = []
for i in range(n):
    line = input().split()
    line = [int(i) for i in line]
    for j in line:
        List.append(j)
#print(List)
List2 = []
num = 0
for i in range(n):
    for j in range(i, n, 1):
        List2.append([i+1, j+1, List[num]])
        num += 1
#print(List2)
#all_ranges[a][b] = range between a and b
all_ranges = [['null'for i in range(n+1)]for j in range(n+1)]
for i in List2:
    all_ranges[i[0]][i[1]] = i[2]
#print(all_ranges)

#all_restraints[index] = [max of index]

#has to be adjacent comparisons
ans = [0, 0]
ans2 = []
x = True
recursion(2, ans)
string = ''
ans2.pop(0)
for i in range(n-1):
    string += str(ans2[i])
    string += ' '
string += str(ans2[-1])
print(string)