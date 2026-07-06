# Last updated: 7/6/2026, 12:27:42 AM
1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        x = 0
4        for n in nums:
5            if len(str(n)) % 2 == 0:
6                x+=1
7        return x