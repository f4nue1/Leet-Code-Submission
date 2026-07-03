# Last updated: 7/3/2026, 2:03:45 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        group = defaultdict(list)
4        for s in strs:
5            key = "".join(sorted(s))
6            group[key].append(s)
7
8        return list(group.values())