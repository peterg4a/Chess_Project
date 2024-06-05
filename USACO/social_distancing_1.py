n = int(input())
line = input()
stalls = [int(i) for i in line]
for i in range(2):
    largest = 0
    position = 'none'
    for i in range(n):
        if stalls[i] == 0:
            num = 1
            while True:
                if num + 1 <= n and num - 1 >= 0:
                    
                if num + 1 <= n and num - 1 < 0:

                if num + 1 > n and num - 1 >= 0:
        print(largest)
    stalls[position] = 1
    print(stalls)


# largest_gap == 0
# start_largest = 0
# gap = 0
# start_gap = 0
# for i in range(n):
#     if i == '0' or stalls[i-1] == '1':
#         if stalls[i] == '0':
#             gap == 1
#             start_gap = i
#     if stalls[i-1] == '0' and stalls[i] == '0':
#         gap += 1
#     if stalls[i-1] == '0' and stalls[i] == '1':
#         if gap > largest_gap:
#             largest_gap = gap
#             start_largest = start_gap
    
