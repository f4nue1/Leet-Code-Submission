# Last updated: 10/28/2026, 4:33:37 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        curr = 0
4        for i in range(k):
5            curr += nums[i]
6            
7        ans = curr
8        
9        for i in range(k, len(nums)):
10            curr += nums[i] - nums[i - k]
11            ans = max(ans, curr)
12            
13        return ans / k
14            
15        avg = curr_sum / k
16        max_avg = max(max_avg, avg)
17        
18        return max_avg
19        
20        
21    