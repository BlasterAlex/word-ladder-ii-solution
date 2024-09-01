# Word Ladder II Solution

Possible solution to LeetCode problem: [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/description)

## Problem Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of
words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every $s_i$ for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return all the shortest transformation
sequences from
`beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the
words `[beginWord, s1, s2, ..., sk]`.

### Example 1

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

### Example 2

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

### Constraints

- `1 <= beginWord.length <= 5`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 500`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are unique.
- The sum of all shortest transformation sequences does not exceed $10^5$.

## Proposed solution

### Main idea

If we consider transformation sequences as the path from point `beginWord` to point `endWord`, then the problem reduces
to finding the shortest path. The [breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) algorithm
is great for this purpose, but simply searching all possible paths from `beginWord` is not an optimal solution, since
not all paths will lead to `endWord`.

To reduce the number of dead-end paths to be processed, we propose an approach with sequential breadth-first search
starting from `beginWord` and `endWord` simultaneously until the intersection points of the paths are found.

### Finding adjacent pairs (neighbors)

Words are considered neighbors if they differ by a single letter. To quickly find all neighboring words, it is suggested
to pre-store `wordList` in **set collection**, and also save all possible letters **for each position** in word.

Thus, for each word it is possible to find a list of its neighbors, making a sequential search for words differing by
one
letter for each position.

#### Example

```
word: hot
wordSet: {hit, dot, dog, lot, log, cog}
positionLetters:
  0: {c, d, h, l}
  1: {i, o}
  2: {g, t}

neighbors by letter position 0:
    possible: cot, dot, lot
    existing: dot, lot
neighbors by letter position 1:
    possible: hit
    existing: hit
neighbors by letter position 2:
    possible: hog
    existing: no words

hot neighbors 🔥:
    {dot, lot, hit}

```

### Finding the shortest paths

To implement breadth-first search, **queue collection** will be used to store the order in which words are processed.

Since the search is performed from `beginWord` forward and `endWord` backward simultaneously, the following information
is stored for each processed word:

```python
from typing import NamedTuple


class QueuedWord(NamedTuple):
    word: str
    "Processed word"

    forward: bool
    "Search direction: forward/backward"

    level: int = 1
    "Level in path relative to beginning/end"
```

#### Storing word paths

To organize optimal storage of information about transformation sequences for each word, two dictionaries are used
`forwardWordPaths` and `backwardWordPaths`.

A word key stores the set of all possible paths to that word of minimum length from the beginning/end depending on
travel direction (forward/backward).

This solves the problem of storing duplicate information about paths that have common parts. For example:

```

```

##### Example

```
beginWord: hit
endWord: cog
wordSet: {hot, lot, log, cog}

forwardWordPaths[hot]: hit -> hot
forwardWordPaths[lot]: hit -> hot -> lot

backwardWordPaths[log]: log <- cog
backwardWordPaths[lot]: lot <- log <- cog
```

#### Processing word in queue

Pairs of adjacent words with `beginWord` and `endWord` are added to queue before processing is started.

> If `endWord` is not in `wordList`, processing ends with an empty list result.

> If `beginWord` and `endWord` are adjacent, such a sequence is returned as the result and processing ends.

The processing of a word in a queue occurs in several steps:

- Checking search completion condition
- Searching for adjacent words (neighbors)
- For each adjacent word found, a check is performed to ensure that the given path has not been checked before
- If this is the first visit to this word in the path, the word is added to the end/start of the neighbor path list,
  depending on the current travel direction (forward/backward)

#### Search completion condition
