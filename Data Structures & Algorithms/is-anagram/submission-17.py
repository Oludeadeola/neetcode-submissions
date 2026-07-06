class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        uniq_valuet = defaultdict(int)
        uniq_values= defaultdict(int)
        for i in t:
            uniq_valuet[i]+=1
        for j in s:
            uniq_values[j]+=1
        if uniq_valuet == uniq_values:
            return True
        return False        

