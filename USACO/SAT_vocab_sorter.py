f = open('SATvocab.txt', 'r')
vocab_list = f.readlines()
vocab = {}
for i in range(0, len(vocab_list)-1, 3):
    vocab[vocab_list[i]] = vocab_list[i+1]
    print(vocab_list[i], vocab_list[i+1], vocab_list[i+2])
f.close()

while True:
    f = open('SATvocab.txt', 'r')
    vocab_list = f.readlines()
    f.close()
    word = input('Enter the new word : ') + '\n'
    #backup function
    if word == 'backup\n':
        f = open('SATvocab_safety.txt', 'w')
        for i in vocab_list:
            f.write(i)
        f.close()
    #####
    else:
        definition = input('Enter the new definition : ') + '\n'
        vocab[word] = definition
        keys = list(vocab.keys())
        print(vocab)
        keys.sort()
        f = open('SATvocab.txt', 'w')
        f.truncate(0)
        for i in keys:
            f.write(i)
            f.write(vocab[i])
            f.write('\n')
        f.close()