from typing import List, Set, NamedTuple
import queue


class QueuedWord(NamedTuple):
    word: str
    "Processed word"

    forward: bool
    "Search direction: forward/backward"

    level: int = 1
    "Level in path relative to beginning/end"


class Solution:
    def __init__(self):
        self.positionLetters = []
        self.wordNeighborsCache = {}
        self.wordSet = set()

        self.wordQueue = queue.Queue()
        self.forwardWordPaths = {}
        self.backwardWordPaths = {}
        self.forwardVisited = {}
        self.backwardVisited = {}

    def prepareData(self, beginWord: str, endWord: str, wordList: List[str]):
        self.positionLetters = []
        self.wordNeighborsCache = {}
        self.wordSet = set(wordList)

        for word in wordList:
            for i, c in enumerate(word):
                if i >= len(self.positionLetters):
                    self.positionLetters.append({c})
                elif c not in self.positionLetters[i]:
                    self.positionLetters[i].add(c)

        self.forwardWordPaths = {}
        self.backwardWordPaths = {}
        self.forwardVisited = {}
        self.backwardVisited = {}

        if not self.wordQueue.empty():
            self.wordQueue = queue.Queue()

        for w in self.findWordNeighbors(beginWord):
            self.forwardWordPaths[w] = [[beginWord, w]]
            self.wordQueue.put(QueuedWord(w, True))

        for w in self.findWordNeighbors(endWord):
            self.backwardWordPaths[w] = [[w, endWord]]
            self.wordQueue.put(QueuedWord(w, False))

    def findWordNeighbors(self, word: str) -> Set[str]:
        if word in self.wordNeighborsCache:
            return self.wordNeighborsCache[word]

        neighbors = set()
        for i, c in enumerate(word):
            for opt in self.positionLetters[i]:
                if c == opt:
                    continue
                w = word[:i] + opt + word[i + 1:]
                if w in self.wordSet:
                    neighbors.add(w)

        self.wordNeighborsCache[word] = neighbors
        return neighbors

    def visitNeighbor(self, qWord: QueuedWord, neighbor: str) -> bool:
        """Checking that this neighbor has not been visited before in this path"""
        visited = self.forwardVisited if qWord.forward else self.backwardVisited
        word = qWord.word
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

    def wordProcessing(self, qWord: QueuedWord):
        word = qWord.word
        forward = qWord.forward
        level = qWord.level

        for neighbor in self.findWordNeighbors(word):
            if self.visitNeighbor(qWord, neighbor):
                continue

            wordPaths = self.forwardWordPaths if forward else self.backwardWordPaths
            if forward:
                wPaths = [wpath + [neighbor] for wpath in wordPaths[word]]
            else:
                wPaths = [[neighbor] + wpath for wpath in wordPaths[word]]
            if len(wPaths) == 0:
                continue

            self.wordQueue.put(QueuedWord(neighbor, forward, level + 1))
            if neighbor in wordPaths:
                if len(wPaths[0]) == len(wordPaths[neighbor][0]):
                    wordPaths[neighbor] += wPaths
            else:
                wordPaths[neighbor] = wPaths

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # beginWord and endWord are adjacent
        if sum(b != e for b, e in zip(beginWord, endWord)) == 1:
            return [[beginWord, endWord]]

        self.prepareData(beginWord, endWord, wordList)

        result = []
        foundWords = set()
        foundLevel = 0
        foundForward = False

        # word queue processing
        while not self.wordQueue.empty():
            qWord = self.wordQueue.get()
            if foundLevel > 0:
                if qWord in foundWords or qWord.forward != foundForward or qWord.level > foundLevel:
                    continue
            if self.wordFound(qWord):
                foundWords.add(qWord)
                foundLevel, foundForward = qWord.level, qWord.forward
                result += [forwardPaths + backwardPaths[1:] for forwardPaths in self.forwardWordPaths[qWord.word] for
                           backwardPaths in self.backwardWordPaths[qWord.word]]
            else:
                self.wordProcessing(qWord)

        return result
