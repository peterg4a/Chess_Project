alphabet = 'abcdefghijklmnopqr'
a = {}
for i in range(18):
    a[alphabet[i]] = i+1

s = [a[i] for i in input()]
t = [a[i] for i in input()]
n = int(input())
ans = ''
for i in range(n):
    query = [a[i] for i in input()]
    #s
    s_new = []
    for j in s:
        if j in query:
            s_new.append(j)

    #t
    t_new = []
    for j in t:
        if j in query:
            t_new.append(j)
    # print(s_new, t_new)
    if s_new == t_new:
        ans += 'Y'
    else:
        ans += 'N'
print(ans)