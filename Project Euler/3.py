num = 600851475143
for i in range(600851475143):
    if i != 0:
        if num%i == 0:
            num /= i
            print(i)