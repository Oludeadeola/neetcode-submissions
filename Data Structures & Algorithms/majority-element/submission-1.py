from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_key = defaultdict(int)
        largest_element = 0
        for i in nums:
            hash_key[i] +=1
        for key, count in hash_key.items():
            if count > len(nums)/2:
                return key