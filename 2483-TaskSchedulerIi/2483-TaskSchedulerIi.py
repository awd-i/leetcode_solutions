# Last updated: 11/11/2025, 1:55:26 AM
class Solution:

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        nextday = {}
        days = 0
        for task in tasks:
            if task in nextday:
                if nextday[task] > days:
                    days = nextday[task]
            days += 1
            nextday[task] = days + space

        return days
            



