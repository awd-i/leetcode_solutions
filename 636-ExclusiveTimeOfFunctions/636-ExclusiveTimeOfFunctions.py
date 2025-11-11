# Last updated: 11/11/2025, 1:56:02 AM
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        stack = []
        prev_time = 0

        for log in logs:
            uid, event, time = log.split(":")
            uid, time = int(uid), int(time)
            if event == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(uid)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1 # stack.pop when theres an end, time - prev_time + 1
                prev_time = time + 1
            
        return ans




