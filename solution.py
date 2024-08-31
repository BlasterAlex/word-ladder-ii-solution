from typing import List, Set
import queue


class Solution:
    def __init__(self):
        self.positionLetters = []
        self.wordNeighbors = {}
        self.wordSet = set()

    def prepareData(self, endWord: str, wordList: List[str]) -> bool:
        if endWord not in wordList:
            return False

        self.positionLetters = []
        self.wordNeighbors = {}
        self.wordSet = set(wordList)

        for word in wordList:          
            for i, c in enumerate(word):
                if i >= len(self.positionLetters):
                    self.positionLetters.append({c})
                elif c not in self.positionLetters[i]:
                    self.positionLetters[i].add(c)
        return True
    
    def findWordNeighbors(self, word: str) -> Set[str]:
        if word in self.wordNeighbors:
            return self.wordNeighbors[word]

        neighbors = set()          
        for i, c in enumerate(word):
            for opt in self.positionLetters[i]:
                if c == opt:
                    continue
                w = word[:i] + opt + word[i+1:]
                if w in self.wordSet:
                    neighbors.add(w)

        self.wordNeighbors[word] = neighbors
        return neighbors

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not self.prepareData(endWord, wordList):
            return []
        
        wordQueue = queue.Queue()
        wordPaths = dict()
        visitedNeighbors = dict()

        for w in self.findWordNeighbors(beginWord):
            wordPaths[w] = [[beginWord, w]]
            wordQueue.put(w)
        
        while not wordQueue.empty():         
            word = wordQueue.get()
            if word == endWord:
                return wordPaths[word]
 
            for w in self.findWordNeighbors(word):
                if word in visitedNeighbors:
                    if w in visitedNeighbors[word]:
                        continue
                    else:
                        visitedNeighbors[word].add(w)
                else:
                    visitedNeighbors[word] = {w}

                wpaths = [wpath + [w] for wpath in wordPaths[word] if w not in wpath]
                if len(wpaths) == 0:
                    continue

                wordQueue.put(w)
                if w in wordPaths:
                    minPathLen = len(wpaths[0])
                    for p in wordPaths[w]:
                        if len(p) < minPathLen:
                            break
                    else:
                        wordPaths[w] += wpaths
                else:
                    wordPaths[w] = wpaths
        
        return []