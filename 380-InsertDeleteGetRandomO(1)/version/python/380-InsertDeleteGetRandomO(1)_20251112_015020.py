# Last updated: 11/12/2025, 1:50:20 AM
class RandomizedSet:
    def __init__(self):
        self.pos = {}      
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # move last into idx
        self.arr[idx] = last
        self.pos[last] = idx

        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)