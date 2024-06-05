starting_times = []
finishing_times = []
buckets_required = []
f = open('blist.in')
n = int(f.readline())
for i in range(n):
    a = f.readline()
    a = a.split()
    starting_times.append(int(a[0]))
    finishing_times.append(int(a[1]))
    buckets_required.append(int(a[2]))
f.close

max_buckets_used = 0
buckets_in_use = 0
for time in range(max(finishing_times) + 1):

    for i in range(n):
        if starting_times[i] == time:
            buckets_in_use = buckets_in_use + buckets_required[i]
    
    for i in range(n):
        if finishing_times[i]== time:
            buckets_in_use = buckets_in_use - buckets_required[i]

    if buckets_in_use > max_buckets_used:
        max_buckets_used = buckets_in_use

f = open('blist.out','w')
f.write(str(max_buckets_used))
f.close()


