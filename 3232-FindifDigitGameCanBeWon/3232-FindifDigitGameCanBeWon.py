# Last updated: 7/6/2026, 12:30:58 AM
1class Solution:
2    def canAliceWin(self, nums: List[int]) -> bool:
3        x = 0
4        y = 0
5        for n in nums:
6            if len(str(n)) == 1:
7                x += n
8            else:
9                y += n
10        if x > y or y > x:
11            return True
12        else:
13            return False