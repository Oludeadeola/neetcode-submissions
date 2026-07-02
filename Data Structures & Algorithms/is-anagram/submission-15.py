class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        if len(s) != len(t):
            return False
        return sorted(s)== sorted(t)
#time complexity : O(nlogn+mlogm)
#space complexity O(1)        