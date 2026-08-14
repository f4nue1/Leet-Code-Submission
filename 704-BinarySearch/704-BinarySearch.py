# Last updated: 8/13/2026, 9:07:26 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left <= right:
6            mid = (left + right) // 2
7            num = nums[mid]
8            if num == target:
9                return mid
10            elif num > target:
11                right = mid - 1
12            elif num < target:
13                left = mid + 1
14        return -1