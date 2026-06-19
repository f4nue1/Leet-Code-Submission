# Last updated: 6/18/2026, 8:02:42 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        nums1.extend(nums2)
4        nums1.sort()
5        x = len(nums1)
6        if(x % 2 == 1):
7            return float(nums1[x // 2])
8        elif (len(nums1) % 2 == 0):
9            y = x // 2 -1
10            z = x // 2
11            a = (nums1[y] + nums1[z]) / 2
12            return float(a)