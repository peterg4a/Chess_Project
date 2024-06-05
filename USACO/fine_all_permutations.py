def find(x):
    if len(x) < len(List):
        new = List[len(x)]
        for i in range(len(List)+1):
            x_copy = [i for i in x]
            x_copy.insert(i, new)
            find(x_copy)
    else:
        permutations.append(x)

string = input()
List = [i for i in string]
permutations = []
find([])
permutations.sort()
for i in permutations:
    print(permutations)