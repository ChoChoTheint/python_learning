words = ['apple','banana','lemon']
from random import randint;
def randomSentenceGengerator(word):
    randomIndex = randint(0,len(words)-1)
    return f'{words[randomIndex]} {word}'



with open('./text.txt') as file:
    paragraph = file.read();
    wordLists = paragraph.split()
    sentenceList = list(map(randomSentenceGengerator,wordLists))
    paraCount = int(input('paragraph count : '))
    
    for count in range(paraCount):
        with open('./generator.txt','a') as  write_file:
            write_file.write(''.join(sentenceList) +'\n\n')