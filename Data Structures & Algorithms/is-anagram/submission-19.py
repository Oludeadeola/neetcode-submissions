class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        seen_t = defaultdict(int)
        seen_s = defaultdict(int)
        for i in s:
            seen_s[i]+=1
        for j in t :
            seen_t[j]+=1
        if seen_t==seen_s:
            return True
        return False            