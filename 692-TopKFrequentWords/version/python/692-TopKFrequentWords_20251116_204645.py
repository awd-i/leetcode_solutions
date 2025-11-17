# Last updated: 11/16/2025, 8:46:45 PM
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:


        cnt = Counter(words)
        heap = [(-freq,word) for word, freq in cnt.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
