k_n_input = input()
k_n_input = k_n_input.split()
k = int(k_n_input[0])
n = int(k_n_input[1])

contests = []

for a in range(k):
    contest_input = input()
    contest_input = contest_input.split()
    contest_input = [int(i) for i in contest_input ]
    contests.append(contest_input)
        
    placements.append(p)

for k in range(k):
    contest = contests[k]
    for n in range(n):
        number = 1
        original_cow = contest[n]
        other_cow = contest[]