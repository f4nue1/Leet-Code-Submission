# Last updated: 11/5/2026, 12:47:25 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        matching = {"(": ")", "[": "]", "{":"}"}
5
6        for c in s:
7            if c in matching:
8                 stack.append(c)
9            else:
10                if not stack:
11                    return False
12                
13                previous = stack.pop()
14                if matching[previous] != c:
15                    return False
16        return not stack