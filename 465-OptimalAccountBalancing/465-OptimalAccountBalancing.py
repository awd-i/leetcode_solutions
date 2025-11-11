# Last updated: 11/11/2025, 1:56:10 AM
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = collections.defaultdict(int)
        for a, b, amount in transactions:
            balance_map[a] += amount
            balance_map[b] -= amount
        balance_list = [amount for amount in balance_map.values() if amount] # take a list of everyone who owes
        n = len(balance_list)
        def dfs(curr):
            while curr < n and not balance_list[curr]:
                curr += 1
            if curr == n:
                return 0
            cost = float('inf')
            for nxt in range(curr + 1, n):
                if balance_list[nxt] * balance_list[curr] < 0:
                    balance_list[nxt] += balance_list[curr]
                    cost = min(cost, 1 + dfs(curr + 1))
                    balance_list[nxt] -= balance_list[curr]
            return cost
        return dfs(0)

