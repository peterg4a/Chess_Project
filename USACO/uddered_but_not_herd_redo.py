line = input()
word = input()
x = 26
ans = 0
for i in word:
    if line.index(i) <= x:
        ans += 1
    x = line.index(i)
print(ans)