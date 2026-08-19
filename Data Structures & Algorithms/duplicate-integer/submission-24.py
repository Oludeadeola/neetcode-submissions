class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        seen = defaultdict(int)
        for i in nums:
            seen[i]+=1
        for key,value in seen.items():
            if value>1:
                return True
        return False        