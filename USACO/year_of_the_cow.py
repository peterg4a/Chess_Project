n = int(input())
sentences = []
zodiac = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
people_zodiac = {}
positions = {}
for i in range(n):
    sentence = input()
    sentence = sentence.split()
    sentences.append(sentence)

    people_zodiac[sentence[0]] = sentence[4]
    if sentence[7] == 'Bessie':
        positions[sentence[0]] = 0
    if sentence[7] != 'Bessie':
        if sentence[3] == 'next':
            distance = 0
            position = people_zodiac[sentence[7]]
            while True:
                distance = distance + 1
                position = position + 1
                if position == 12:
                    position = 0
                if zodiac[position] == sentence[4]:
                    break
            positions[sentence[7]] = positions[sentence[0] + distance]
        
        if sentence[3] == 'previous':
            distance = 0
            position = people_zodiac[sentence[7]]
            while True:
                distance = distance + 1
                position = position - 1
                if position == -1:
                    position = 11
                if zodiac[position] == sentence[4]:
                    break
            positions[sentence[0]] = positions[sentence[7]] - distance
    
print(positions)

