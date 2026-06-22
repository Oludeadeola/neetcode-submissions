from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_t = defaultdict(int)
        unique_s = defaultdict(int)
        for i in t:
            unique_t[i] +=1 
        for j in s :
            unique_s[j] +=1   
        if unique_t == unique_s :
            return True
        else:
            return False      

