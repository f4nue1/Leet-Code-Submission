# Last updated: 7/5/2026, 3:16:46 PM
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        ransomeNote = list(ransomNote)
4        magazine = list(magazine)
5        for n in ransomNote:
6            if n not in magazine:
7                return False
8            else:
9                magazine.remove(n)
10        return True