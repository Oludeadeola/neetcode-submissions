from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)
        for i in range(len(nums)):
         hash_map[nums[i]] +=1
        for value in hash_map:
          if hash_map[value]> 1:
            return True
        return False      