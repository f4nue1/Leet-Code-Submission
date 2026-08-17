# Last updated: 8/17/2026, 2:48:12 PM
1class Solution:
2    def minStartValue(self, nums: List[int]) -> int:
3        sum, ans = 0, 0
4
5        for n in nums:
6            sum += n
7            ans = min(ans, sum)
8        return -ans + 1