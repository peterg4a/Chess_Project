f = open('mixmilk.in')
buckets = []
milks = []
for i in range(3):
    line = f.readline()
    line = line.split()
    bucket_capacity = int(line[0])
    buckets.append(bucket_capacity)
    milk = int(line[1])
    milks.append(milk)
f.close()

for i in range(100):
    bucket_number = i % 3
    next_bucket_number = (i + 1) % 3
    if milks[bucket_number] > buckets[next_bucket_number] - milks[next_bucket_number]:

        milks[bucket_number] = milks[bucket_number] - (buckets[next_bucket_number] - milks[next_bucket_number])
        milks[next_bucket_number] = buckets[next_bucket_number]


    if milks[bucket_number] <= buckets[next_bucket_number] - milks[next_bucket_number]:

        milks[next_bucket_number] = milks[next_bucket_number] + milks[bucket_number]
        milks[bucket_number] = 0

f = open('mixmilk.out', 'w')
for i in range(3):
    f.write(str(milks[i])+'\n')
f.close
