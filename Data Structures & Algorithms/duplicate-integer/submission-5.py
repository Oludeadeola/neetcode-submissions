from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        for num in freq:
            if freq[num] >1 :
                return True
        return False            