from typing import List, Set, Dict, NamedTuple
import queue


class QueuedWord(NamedTuple):
    """Word in processing queue"""

    word: str
    "Processed word"

    forward: bool
    "Search direction: forward/backward"

    level: int = 1
    "Level in path relative to beginning/end"


class WordTreeNode(NamedTuple):
    """Word in hierarchy tree"""

    children: Set = set()
    "Child words in hierarchy tree"

    level: int = 1
    "Level in hierarchy tree"


class Solution:
    wordSet: Set[str]
    positionLetters: List[Set[str]]
    wordNeighborsCache: Dict[str, Set[str]]
    forwardWordTree: Dict[str, WordTreeNode]
    backwardWordTree: Dict[str, WordTreeNode]
    wordQueue = queue.Queue()

    def prepareData(self, beginWord: str, endWord: str, wordList: List[str]):
        """Required data initialization"""

        self.positionLetters = []
        self.wordNeighborsCache = {}
        self.wordSet = set(wordList)

        for word in wordList:
            for i, c in enumerate(word):
                if i >= len(self.positionLetters):
                    self.positionLetters.append({c})
                elif c not in self.positionLetters[i]:
                    self.positionLetters[i].add(c)

        self.forwardWordTree = {}
        self.backwardWordTree = {}

        if not self.wordQueue.empty():
            self.wordQueue = queue.Queue()

        for w in self.findWordNeighbors(beginWord):
            self.forwardWordTree[w] = WordTreeNode({beginWord})
            self.wordQueue.put(QueuedWord(w, True))

        for w in self.findWordNeighbors(endWord):
            self.backwardWordTree[w] = WordTreeNode({endWord})
            self.wordQueue.put(QueuedWord(w, False))

    def findWordNeighbors(self, word: str) -> Set[str]:
        """Getting a list of all adjacent words with result caching"""

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

    def wordPathFound(self, qWord: QueuedWord) -> bool:
        """Checking the condition for finding a new path intersection"""

        if qWord.forward:
            return qWord.word in self.backwardWordTree
        else:
            return qWord.word in self.forwardWordTree

    def wordProcessing(self, qWord: QueuedWord):
        """Processing word from word queue"""

        word = qWord.word
        forward = qWord.forward
        neighborLevel = qWord.level + 1

        for neighbor in self.findWordNeighbors(word):
            wordTree = self.forwardWordTree if forward else self.backwardWordTree
            if word in wordTree:
                if neighbor in wordTree[word].children:
                    continue

            if neighbor in wordTree:
                node = wordTree[neighbor]
                if node.level == neighborLevel:
                    node.children.add(word)
            else:
                wordTree[neighbor] = WordTreeNode({word}, neighborLevel)
                self.wordQueue.put(QueuedWord(neighbor, forward, neighborLevel))

    def buildCrossPaths(self, point: str) -> List[List[str]]:
        """Getting a list of all word paths that intersect at the given point"""

        forwardPaths = self.buildWordPaths(point, True)
        backwardPaths = self.buildWordPaths(point, False)
        return [forwardPath + backwardPath[1:] for forwardPath in forwardPaths for backwardPath in backwardPaths]

    def buildWordPaths(self, word: str, forward: bool) -> List[List[str]]:
        """Getting a list of all word path """

        wordTree = self.forwardWordTree if forward else self.backwardWordTree
        if word not in wordTree:
            return [[word]]

        result = []
        node = wordTree[word]

        for child in node.children:
            childPaths = self.buildWordPaths(child, forward)
            if forward:
                result += [childPath + [word] for childPath in childPaths]
            else:
                result += [[word] + childPath for childPath in childPaths]

        return result

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # beginWord and endWord are adjacent
        if sum(b != e for b, e in zip(beginWord, endWord)) == 1:
            return [[beginWord, endWord]]

        self.prepareData(beginWord, endWord, wordList)

        result = []
        pathsFound = set()
        foundLevel = 0
        foundForward = False

        # word queue processing
        while not self.wordQueue.empty():
            qWord = self.wordQueue.get()
            if foundLevel > 0:
                # given path has already been found or all possible points of the same level have been processed
                if qWord in pathsFound or qWord.forward != foundForward or qWord.level > foundLevel:
                    continue
            if self.wordPathFound(qWord):
                # word path intersection point is found, save the paths
                result += self.buildCrossPaths(qWord.word)
                foundLevel, foundForward = qWord.level, qWord.forward
                pathsFound.add(qWord)
            else:
                # processing word from queue
                self.wordProcessing(qWord)

        return result
