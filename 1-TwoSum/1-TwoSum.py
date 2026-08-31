# Last updated: 8/31/2026, 4:01:24 AM
1class Solution(object):
2    def twoSum(self, nums, target):
3        self.nums = nums
4        self.target = target
5        """
6        :type nums: List[int]
7        :type target: int
8        :rtype: List[int]
9        """
10        
11        dic = {}
12        for i in range(len(nums)):
13            num = nums[i]
14            x = target - num
15            if x in dic:
16                return[i, dic[x]]
17            dic[num] = i
18
19        