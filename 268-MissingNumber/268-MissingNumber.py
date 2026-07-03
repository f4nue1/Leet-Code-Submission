# Last updated: 7/3/2026, 1:33:47 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3       for i in range(len(nums)+1):
4        if i not in nums:
5            return i
6    
7