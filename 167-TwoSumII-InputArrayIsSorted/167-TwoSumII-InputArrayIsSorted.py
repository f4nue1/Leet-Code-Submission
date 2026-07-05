# Last updated: 7/5/2026, 4:04:54 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        left = 0
7        right = 0
8        while right < len(nums):
9            if nums[right] != 0:
10                nums[left] = nums[right]
11                left += 1
12            right += 1
13        while left < len(nums):
14            nums[left] = 0
15            left += 1
16        return nums        
17        