# Last updated: 7/5/2026, 3:19:57 PM
1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        x = 0
4        y = []
5        for i in range(len(accounts)):
6            for j in range(len(accounts[i])):
7                x += accounts[i][j]
8            y.append(x)
9            x = 0
10        return max(y)
11