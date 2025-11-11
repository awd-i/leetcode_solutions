# Last updated: 11/11/2025, 1:55:53 AM
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]
        for ch, c in count.items():
            result.append(ch * c)
        return "".join(result)