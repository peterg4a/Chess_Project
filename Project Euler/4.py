def palindromic(num):
    if str(num) == ''.join(reversed(str(num))):
        return True
    else:
        return False

largest = 0
for num1 in range(1000):
    for num2 in range(1000):
        if palindromic(num1*num2):
            if num1*num2 > largest:
                largest = num1*num2
print(largest)