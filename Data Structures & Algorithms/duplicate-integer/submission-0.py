from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic_int = defaultdict(int)
        for i in range(len(nums)):
            dic_int[nums[i]] += 1
        for key in dic_int:
            if dic_int[key] >1:
                return True
        return False    