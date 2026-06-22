class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       word1 = sorted(s)
       word2 = sorted(t)
       for i in range(len(word1)):
        if word1 == word2:
            return True
       return False 