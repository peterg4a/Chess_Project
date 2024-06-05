def calc(pos, cur_cost, past_pos, count):
    if count < 15:
        for i in move:
            fpos = [pos[j]+i[j] for j in range(2)]
            if fpos not in past_pos and fpos[0]>-1 and fpos[0]<6 and fpos[1]>-1 and fpos[1]<6:
                print(pos, fpos, count)
                new_past_pos = [j for j in past_pos]
                new_past_pos.append(fpos)
                new_cost = cur_cost + Map[fpos[1]][fpos[0]] * (Map[fpos[1]][fpos[0]]%4 +1)
                if fpos == fin:
                    total_costs.append(new_cost)
                else:
                    calc(fpos, new_cost, new_past_pos, count+1)
    else:
        print(pos, cur_cost, past_pos, count)

Map = []
for i in range(6):
    line = input()
    line = line.split()
    line = [int(i) for i in line]
    Map.append(line)

line = input()
line = line.split()
line = [int(i) for i in line]
sta = [line[0], line[1]] 
fin = [line[2], line[3]]

move = [[0,1], [0,-1], [1,0], [-1,0]]
total_costs = []

calc(sta, 0, [sta], 0)
print(total_costs)
print(min(total_costs))

#How it should be done
# sx,sy
# nx, ny

# Grid # 6 * 6,
# vis # 6 * 6 initial value = 0

# status # 6 * 6

# status[0][0] = 1
# vis[sx][sy] = 1;

# ans = 1000000000

# def dfs(x, y):
#     if x ==tx and y == ty:
#         ans = min(ans, cur_accu_cost)
#         return

        
#     for dx,dy in move:
#         nx = x + dx
#         ny = y + dy
        
#         if nx >= 1 and nx <= 6 and ny >= 1 and ny <= 6 and vis[nx][ny] == 0:
#             vis[nx][ny] = 1
#             cur_cost += 
#             dfs(nx, ny)
#             vis[nx][ny] = 0