citations = []
n = int(input('Number of published papers : '))
l = int(input('Number of citations that can be added : '))
for i in range(n):
    citation_number = int(input('Enter the number of citations for a paper : '))
    citations.append(citation_number)


h = 1
while True:
    citations2 = list(citations)
    print('1 is',citations)
    print('2 is', citations2)
    for i in range(n):
        if n > h:
            k = 0
            for i in range(n):
                citation_number = citations[i]
                if citation_number > n:
                    k = k+ 1
                    print(citation_number)
                    citations2.remove(citation_number)
            
            if k > n:
                n = n + 1
            
            if k < n or k == n:
                if l > 0:
                    biggest_number = 0
                    for i in range(n):
                        citation_number = citations2[i]
                        if citation_number > biggest_number:
                            biggest_number = citation_number
                            biggest_number_position = i
                    
                    citations[biggest_number_position] = biggest_number + 1
                    l = l - 1
                
                if l == 0:
                    break

        if n < h or n == h:
            break
print('1 is',citations)
print('2 is', citations2)
print(h)