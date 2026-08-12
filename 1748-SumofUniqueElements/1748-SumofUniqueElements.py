# Last updated: 8/12/2026, 5:30:56 PM
1class Solution:
2    def sumOfUnique(self, nums: List[int]) -> int:
3        myVal = 0
4        seen = set(nums)
5        for n in seen:
6            if nums.count(n) == 1:
7                myVal += n
8        return myVal