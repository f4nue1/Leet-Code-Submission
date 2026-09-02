# Last updated: 9/2/2026, 3:46:01 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        
6        while left <= right:
7            mid = (left + right) // 2
8            num = nums[mid]
9            
10            if num == target:
11                return mid
12            
13            if num > target:
14                right = mid - 1
15            else:
16                left = mid + 1
17        
18        return -1