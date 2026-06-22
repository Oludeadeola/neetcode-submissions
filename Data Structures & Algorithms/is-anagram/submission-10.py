from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        countt = defaultdict(int)
        if len(s) != len(t):
            return False
        for ch in range(len(s)):
            counts[s[ch]] +=1
            countt[t[ch]] +=1
        return counts == countt        