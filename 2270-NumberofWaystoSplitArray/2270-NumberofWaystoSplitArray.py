# Last updated: 7/8/2026, 10:23:07 AM
1class Solution:
2    def waysToSplitArray(self, nums: List[int]) -> int:
3        prefix = [nums[0]]
4        for i in range(1, len(nums)):
5            prefix.append(nums[i] + prefix[-1])
6
7        ans = 0
8        for i in range(len(nums)-1):
9            left_most = prefix[i]
10            right_most = prefix[-1] - prefix[i]
11            if left_most >= right_most:
12                ans += 1
13        return ans