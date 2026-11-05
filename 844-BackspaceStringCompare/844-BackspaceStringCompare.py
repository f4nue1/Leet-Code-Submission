# Last updated: 11/5/2026, 4:14:18 PM
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        def build(s):
4            stack = []
5            for c in s:
6                if c != "#":
7                    stack.append(c)
8                elif stack:
9                    stack.pop()
10            return "".join(stack)
11        return build(s) == build(t)
12
13            