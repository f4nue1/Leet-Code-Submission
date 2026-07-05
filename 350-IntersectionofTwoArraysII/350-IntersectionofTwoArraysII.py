# Last updated: 7/5/2026, 6:59:04 PM
1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        myL = []
4        if len(nums1) > len(nums2):
5            x = len(nums1)
6            for i in range(x):
7                if nums1[i] in nums2:
8                    myL.append(nums1[i])
9                    nums2.remove(nums1[i])
10        else:
11            x = len(nums2)
12            for i in range(x):
13                if nums2[i] in nums1:
14                    myL.append(nums2[i])
15                    nums1.remove(nums2[i])
16        return myL
17            
18        