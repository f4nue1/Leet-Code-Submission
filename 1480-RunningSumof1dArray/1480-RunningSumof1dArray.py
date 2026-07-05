# Last updated: 7/5/2026, 3:22:56 PM
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        x = 0
4        
5        for i in range(1,len(nums)):
6            x = nums[i-1]+nums[i]
7            nums[i] = x
8        return nums
9        
10