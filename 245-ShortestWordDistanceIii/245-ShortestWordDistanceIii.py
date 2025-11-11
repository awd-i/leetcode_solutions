# Last updated: 11/11/2025, 1:57:07 AM
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest = len(wordsDict)
        last = -1
        last_word = None
        same = (word1 == word2)

        for i, w in enumerate(wordsDict):
            if w == word1 or w == word2:
                if last != -1 and (same or w != last_word):
                    shortest = min(shortest, i - last)
                last = i
                last_word = w

        return shortest