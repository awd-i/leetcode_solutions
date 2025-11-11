# Last updated: 11/11/2025, 1:55:37 AM
from collections import deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.q and not self.unique[self.q[0]]:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.unique:
            self.unique[value] = True
            self.q.append(value)
        else:
            self.unique[value] = False
