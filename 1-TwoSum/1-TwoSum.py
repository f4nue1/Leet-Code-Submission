# Last updated: 7/1/2026, 10:47:17 AM
1class Solution(object):
2    def twoSum(self, nums, target):
3        self.nums = nums
4        self.target = target
5        """
6        :type nums: List[int]
7        :type target: int
8        :rtype: List[int]
9        """
10        a = 0
11        b = 0
12        for i in range(len(nums)):
13            for j in range(i+1, len(nums)):
14                if nums[i] + nums[j] == target:
15                    a = i
16                    b = j
17                    myArr = [a,b]
18        
19        return myArr
20        