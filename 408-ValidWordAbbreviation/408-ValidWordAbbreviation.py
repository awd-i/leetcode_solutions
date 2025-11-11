# Last updated: 11/11/2025, 1:56:15 AM
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while j < len(abbr) and i < len(word):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False
                temp = 0
                while j < len(abbr) and abbr[j].isdigit():
                    temp = temp * 10 + int(abbr[j])
                    j += 1
                i += temp # if the next character after the length isn't the same it's just false, which is why this works
        return j == len(abbr) and i == len(word)





            
