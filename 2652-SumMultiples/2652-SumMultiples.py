# Last updated: 6/17/2026, 9:03:38 PM
1class Solution:
2    def sumOfMultiples(self, n: int) -> int:
3        myArr = []
4        x = 0
5        for i in range(1,n+1):
6            if (i%3 == 0) or (i%5 == 0) or (i%7 == 0):
7                myArr.append(i)
8        for i in range(len(myArr)):
9            x = x + myArr[i]
10        return x
11