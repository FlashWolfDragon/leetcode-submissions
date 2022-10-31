from collections import defaultdict
from math import inf

class WordDistance:

    def __init__(self, wordsDict):
        self.words = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.words[w].append(i)        

    def shortest(self, word1: str, word2: str) -> int:
        if (word1 not in self.words or word2 not in self.words):
            return None
        
        shortest = inf
        for i in self.words[word1]:
            for j in self.words[word2]:
                shortest = min(abs(i - j), shortest)
        
        return shortest
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

wd = WordDistance(['a', 'b', 'c', 'a'])
res = wd.shortest('a', 'c')
print(res)