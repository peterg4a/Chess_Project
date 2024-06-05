buckets1 = input()
buckets1 = buckets1.split()
buckets1 = [int(i) for i in buckets1]
buckets2 = input()
buckets2 = buckets2.split()
buckets2 = [int(i) for i in buckets2]


def split_buckets1(possibility,buckets):
    different_buckets = []
    for i in range(buckets):
        if buckets[i] not in different_buckets:
            different_buckets.append(buckets[i])
    
    for i in range(len(different_buckets)):
        possibilities.append(possibility - different_buckets[i])
    
    return(possibilities)

def split_buckets2(possibility,buckets):
    different_buckets = []
    for i in range(buckets):
        if buckets[i] not in different_buckets:
            different_buckets.append(buckets[i])
    
    for i in range(len(different_buckets)):
        possibilities.append(possibility + different_buckets[i])
    
    return(possibilities)


possibilities = [1000]
split