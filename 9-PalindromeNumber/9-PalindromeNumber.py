# Last updated: 6/16/2026, 11:21:31 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        myBool = False
4        x = list(str(x))
5        y = x[::-1]
6        if( x == y):
7            myBool = True
8        return myBool