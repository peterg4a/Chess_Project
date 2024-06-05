n = int(input())
flowers_input = input()
flowers_input = flowers_input.split()
flowers = []
for i in range(n):
    flower = flowers_input[i]
    flower = int(flower)
    flowers.append(flower)

average_flower_count = 0

for i in range(n):
    for j in range(i,n):
        total_pedals = 0
        for a in range(i,j+1):
            total_pedals = total_pedals + flowers[a]
        
        average_petals = total_pedals / (j - i + 1)

        for a in range(i,j+1):
            if flowers[a] == average_petals:
                average_flower_count = average_flower_count + 1
                break
        
print(average_flower_count)
