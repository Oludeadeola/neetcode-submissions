class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value = {} ## to track the key and vlaue pair
        
        for key,value in enumerate(nums):
            index_value[value] = key
        
        for key,value in enumerate(nums):
            diff = target-value
            if diff in  index_value and index_value[diff] != key:
                 return [key,index_value[diff]]
        return []         