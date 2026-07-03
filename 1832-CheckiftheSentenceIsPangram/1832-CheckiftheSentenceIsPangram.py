# Last updated: 7/3/2026, 1:18:08 PM
1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        return len(set(sentence)) == 26