# Last updated: 8/17/2026, 5:10:33 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l = 0
4        n = len(s)
5        r = n - 1
6
7        while l < r:
8            if not s[l].isalnum():
9                l += 1
10                continue
11            if not s[r].isalnum():
12                r -= 1
13                continue
14            if s[l].lower() != s[r].lower():
15                return False
16            l += 1
17            r -= 1
18        return True