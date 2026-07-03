# Last updated: 7/3/2026, 1:45:46 PM
1class Solution:
2    def countElements(self, arr: List[int]) -> int:
3        y = 0
4        
5        for nums in arr:
6            if nums + 1 in arr:
7                y+= 1
8        return y
9            