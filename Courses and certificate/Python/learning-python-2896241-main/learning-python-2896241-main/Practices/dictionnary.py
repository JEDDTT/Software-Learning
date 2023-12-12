
wordList = ['lorem', 'ipsum', 'dolor', 'diam', 'amet', 'lorem']
freqMap = {}

for word in set(wordList):
    print(wordList)
    freqMap[word] = wordList.count(word)

print(freqMap)

#print(wordList.count('lorem'))