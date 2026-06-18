# Last updated: 6/17/2026, 7:01:33 PM
1class Solution:
2    def dayOfYear(self, date: str) -> int:
3        mymon = {
4            1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
5            7:31, 8:31, 9:30, 10:31, 11:30, 12:31
6        }
7        b = int(date[0:4])
8        if (b % 4 == 0 and b % 100 != 0) or (b % 400 == 0):
9            mymon[2] = 29
10        x = int(date[5:7])
11        a = 0
12        y = int(date[8:10])
13        for i in range(1, x):
14            a += mymon[i]
15        z = a+y
16        return z
17        