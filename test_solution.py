import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()

    def test_case_1(self):
        [beginWord, endWord] = ["hit", "cog"]
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        self.assertCountEqual(self.solution.findLadders(beginWord, endWord, wordList), expected)

    def test_case_2(self):
        [beginWord, endWord] = ["hit", "cog"]
        wordList = ["hot","dot","dog","lot","log"]
        expected = []
        self.assertCountEqual(self.solution.findLadders(beginWord, endWord, wordList), expected)