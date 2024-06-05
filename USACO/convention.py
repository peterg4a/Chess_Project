# line = input()
# line = line.split()
# line = [int(i) for i in line]
# n, m, c = line
# line = input()
# line = line.split()
# times = [int(i) for i in line]
# times.sort()

# l, r = 0, times[-1]
# while l + 1 > r:
#     mid = (r+l)//2
#     print('Mid ==', mid)
#     busses_used = 1
#     max_waiting_time = 0
#     bus = []
#     for i in range(n):
#         cow = times[i]
#         if bus == []:
#             bus.append(cow)
#         elif cow - bus[0] <= mid and len(bus) <= c:
#             bus.append(cow)
#         else:
#             waiting_time = bus[-1] - bus[0]
#             if waiting_time > max_waiting_time:
#                 max_waiting_time = waiting_time
#             print(bus)
#             bus.clear()
#             busses_used += 1
    

#     if busses_used > m:
#         l = mid
#     elif max_waiting_time < mid:
#         r = mid
#     elif max_waiting_time == mid:
#         print(max_waiting_time)
#         break


def check(x):
    sum = 0
    cnt = 0
    last = 0
    for i in range(1, n+1):
        if t[i] - last <= x and i != 1 and sum < c:
            sum += 1
        else:
            last=t[i]
            sum=1
            cnt +=1

    return cnt <=m

t = [0 for i in range(100000)]

n,m,c = map(int, input().split())
t = list(map(int, input().split()))
t.insert(0,0)

t.sort()

l = 0
r= t[n]


while l +1 < r:
    mid = (l+r )//2

    if check(mid) :
        r = mid
    else:
        l = mid
        
print(r)