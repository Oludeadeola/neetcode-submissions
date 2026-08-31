#check  the k


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        uniq = defaultdict(int)

        for i in nums:
            uniq[i] +=1
        for key,value in uniq.items():
            if value>1:
                return True
        return False             