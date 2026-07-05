# Last updated: 7/5/2026, 4:10:02 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        right = len(nums1) - 1
7        right1 = len(nums2) - 1
8        while right >= m:
9            nums1[right] = nums2[right1]
10            right -= 1
11            right1 -= 1
12        nums1.sort()
13
14        
15        