class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        uniq = defaultdict(int)
        for i in nums:
            uniq[i] +=1

        for i in uniq.values():
            if i >1:
                return True
        return False            
        