# Last updated: 8/12/2026, 5:21:48 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        myBool = False
4        if (len(set(nums)) != len(nums)):
5            myBool = True
6        return myBool
7