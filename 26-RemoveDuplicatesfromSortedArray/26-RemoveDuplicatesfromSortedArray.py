# Last updated: 7/12/2026, 2:33:18 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        slow = 0
4        for fast in range(len(nums)):
5            if nums[slow] != nums[fast]:
6                slow += 1
7                nums[slow] = nums[fast]
8        return slow + 1
9      
10            