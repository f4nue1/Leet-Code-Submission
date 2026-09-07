# Last updated: 9/7/2026, 9:47:09 AM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4        for num in asteroids:
5            if num > mass:
6                return False
7            mass += num
8        return True
9