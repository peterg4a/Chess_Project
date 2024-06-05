shells = ['a','b','c']
shells_copy = ['a','b','c']
n = int(input())
swap1 = []
swap2 = []
guesses = []
for i in range(n):
    swap_guess_input = input()
    swap_guess_input = swap_guess_input.split()

    swap1.append(int(swap_guess_input[0]))
    swap2.append(int(swap_guess_input[1]))
    guesses.append(int(swap_guess_input[2]))

a = 0
b = 0
c = 0

for i in range(n):
    shells_copy[swap1[i] - 1] = shells[swap2[i] - 1]
    shells_copy[swap2[i] - 1] = shells[swap1[i] - 1]

    shells = shells_copy

    guess = shells[guesses[i] - 1]

    if guess == 'a':
        a = a + 1
    if guess == 'b':
        b = b + 1
    if guess == 'c':
        c = c + 1

largest_num = max([a,b,c])

print(largest_num)

# def num_correct(start_shell, A, B, G, n):
#     cur_shell = start_shell
#     correct = 0
#     for i in range(n):
#         if A[i] == cur_shell:
#             cur_shell = B[i]
#         elif B[i] == cur_shell:
#             cur_shell = A[i]
#         if cur_shell == G[i]:
#             correct += 1
#     return correct
    
# n = int(input())
# A = []
# B = []
# G = []
# for i in range(n):
#     line = input().split()
#     #print(line)
#     line = [int(i) for i in line]
#     #print(line)
#     a,b,c = line
#     A.append(a)
#     B.append(b)
#     G.append(c)

# best = 0
# f=open('shell.out', 'w')

# for i in range(1, 4):
#     best = max(best, num_correct(i, A, B, G,n))

# print(best)