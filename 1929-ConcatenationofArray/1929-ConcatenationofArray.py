# Last updated: 7/5/2026, 3:40:23 PM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        y = []
4        oneList = nums[:n]
5        twoList = nums[n:]
6        x = 0
7        for i in range(len(oneList)):
8            y.append(oneList[i])
9            y.append(twoList[i])
10        return y
11        
12