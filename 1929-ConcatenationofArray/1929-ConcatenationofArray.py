# Last updated: 7/5/2026, 3:35:31 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        newNums = nums.copy()
4        for i in range(len(newNums)):
5            nums.append(newNums[i])
6        return nums