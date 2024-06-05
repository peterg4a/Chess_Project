# characteristics = []
# n = int(input())
# for i in range(n):
#     traits = []
#     line = input()
#     line = line.split()
#     for i in range(int(line[1])):
#         traits.append(line[i + 2])
#     characteristics.append(traits)

# max_common_traits = 0
# for a in range(n):
#     traits = characteristics[a]
#     for b in range(n):
#         if b != a:
#             common_traits = 0
#             other_traits = characteristics[b]
        
#             for c in range(len(traits)):
#                 trait = traits[c]
#                 if trait in other_traits:
#                     common_traits = common_traits + 1
    
#             if common_traits > max_common_traits:
#                 max_common_traits = common_traits

# print(max_common_traits)




characteristics = []
f = open('guess.in')
n = int(f.readline())
for i in range(n):
    traits = []
    line = f.readline()
    line = line.split()
    for i in range(int(line[1])):
        traits.append(line[i + 2])
    characteristics.append(traits)
f.close()

max_common_traits = 0
for a in range(n):
    traits = characteristics[a]
    for b in range(n):
        if b != a:
            common_traits = 0
            other_traits = characteristics[b]
        
            for c in range(len(traits)):
                trait = traits[c]
                if trait in other_traits:
                    common_traits = common_traits + 1
    
            if common_traits > max_common_traits:
                max_common_traits = common_traits

f = open('guess.out', 'w')
f.write(str(max_common_traits + 1))
f.close()