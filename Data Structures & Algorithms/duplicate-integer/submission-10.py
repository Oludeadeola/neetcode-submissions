from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_int = defaultdict(int)
        for i in nums:
            freq_int[i] += 1
        for j in freq_int:
            if freq_int[j] >1:
                return True
        return False            