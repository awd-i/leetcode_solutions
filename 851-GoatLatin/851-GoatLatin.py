# Last updated: 11/11/2025, 1:55:52 AM
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if sentence is None:
            return None
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        res = []
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            new_word += "a" * i
            res.append(new_word)
        return " ".join(res)
                




            