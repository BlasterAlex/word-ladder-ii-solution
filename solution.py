from typing import List, Set, NamedTuple
import queue


class QueuedWord(NamedTuple):
    word: str
    forward: bool
    level: int = 1


class Solution:
    def __init__(self):
        self.positionLetters = []
        self.wordNeighborsCache = {}
        self.wordSet = set()
        self.foundLevel = 0

        self.wordQueue = queue.Queue()
        self.backwardWordPaths = {}
        self.forwardWordPaths = {}
        self.backwardVisited = {}
        self.forwardVisited = {}

    def prepareData(self, beginWord: str, endWord: str, wordList: List[str]) -> bool:
        if endWord not in wordList:
            return False

        self.positionLetters = []
        self.wordNeighborsCache = {}
        self.wordSet = set(wordList)

        for word in wordList:          
            for i, c in enumerate(word):
                if i >= len(self.positionLetters):
                    self.positionLetters.append({c})
                elif c not in self.positionLetters[i]:
                    self.positionLetters[i].add(c)

        if not self.wordQueue.empty():
            self.wordQueue = queue.Queue()
        self.forwardWordPaths = {}
        self.backwardWordPaths = {}
        self.forwardVisited = {}
        self.backwardVisited = {}
        self.foundLevel = 0

        for w in self.findWordNeighbors(beginWord):
            self.forwardWordPaths[w] = [[beginWord, w]]
            self.wordQueue.put(QueuedWord(w, True))
            if w == endWord:
                self.foundLevel= 1

        if self.foundLevel == 0:
            for w in self.findWordNeighbors(endWord):
                self.backwardWordPaths[w] = [[w, endWord]]
                self.wordQueue.put(QueuedWord(w, False))

        return True
    
    def findWordNeighbors(self, word: str) -> Set[str]:
        if word in self.wordNeighborsCache:
            return self.wordNeighborsCache[word]

        neighbors = set()          
        for i, c in enumerate(word):
            for opt in self.positionLetters[i]:
                if c == opt:
                    continue
                w = word[:i] + opt + word[i+1:]
                if w in self.wordSet:
                    neighbors.add(w)

        self.wordNeighborsCache[word] = neighbors
        return neighbors

    def visitNeighbor(self, word: str, neighbor: str, forward: bool) -> bool:
        visited = self.forwardVisited if forward else self.backwardVisited
        if word in visited:
            if neighbor in visited[word]:
                return True
            else:
                visited[word].add(neighbor)
        else:
            visited[word] = {neighbor}
        return False

    def wordFound(self, qWord: QueuedWord) -> bool:
        if qWord.forward:
            return qWord.word in self.backwardWordPaths
        else:
            return qWord.word in self.forwardWordPaths

    def wordIteration(self, qWord: QueuedWord):
        word = qWord.word
        forward = qWord.forward
        level = qWord.level

        for neighbor in self.findWordNeighbors(word):
            if self.visitNeighbor(word, neighbor, forward):
                continue

            wordPaths = self.forwardWordPaths if forward else self.backwardWordPaths
            if forward:
                wPaths = [wpath + [neighbor] for wpath in wordPaths[word] if neighbor not in wpath]
            else:
                wPaths = [[neighbor] + wpath for wpath in wordPaths[word] if neighbor not in wpath]
            if len(wPaths) == 0:
                continue

            self.wordQueue.put(QueuedWord(neighbor, forward, level+1))
            if neighbor in wordPaths:
                minPathLen = len(wPaths[0])
                for p in wordPaths[neighbor]:
                    if len(p) < minPathLen:
                        break
                else:
                    wordPaths[neighbor] += wPaths
            else:
                wordPaths[neighbor] = wPaths

    def mergeWordPaths(self, word: str) -> List[List[str]]:
        return [f + b[1:] for f in self.forwardWordPaths[word] for b in self.backwardWordPaths[word]]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not self.prepareData(beginWord, endWord, wordList):
            return []

        result = []
        if self.foundLevel > 0:
            while not self.wordQueue.empty():
                qWord = self.wordQueue.get()
                if qWord.word == endWord:
                    result += self.forwardWordPaths[qWord.word]
            return result

        foundWords = set()
        foundLevel = 0
        foundForward = False

        while not self.wordQueue.empty():
            qWord = self.wordQueue.get()
            if foundLevel > 0:
                if qWord in foundWords or qWord.forward != foundForward or qWord.level > foundLevel:
                    continue
            if self.wordFound(qWord):
                foundWords.add(qWord)
                foundLevel, foundForward = qWord.level, qWord.forward
                result += self.mergeWordPaths(qWord.word)
            else:
                self.wordIteration(qWord)

        return result