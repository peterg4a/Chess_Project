prev_num = 1
num = 2
ans = 2
for i in range(4000000):
    if num > 4000000:
        break
    new_num = prev_num + num
    if new_num%2 == 0:
        ans += new_num
    prev_num = num
    num = new_num
print(ans)